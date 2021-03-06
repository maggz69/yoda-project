__constant sampler_t sampler = CLK_NORMALIZED_COORDS_FALSE | CLK_FILTER_NEAREST | CLK_ADDRESS_CLAMP_TO_EDGE;


kernel void edge_detection(read_only image2d_t in, write_only image2d_t out)
{
    int x = get_global_id(0);
    int y = get_global_id(1);

    if (x >= get_image_width(in) || y >= get_image_height(in))
        return;

    float4 p00 = read_imagef(in, sampler, (int2)(x - 1, y - 1));
    float4 p10 = read_imagef(in, sampler, (int2)(x,     y - 1));
    float4 p20 = read_imagef(in, sampler, (int2)(x + 1, y - 1));

    float4 p01 = read_imagef(in, sampler, (int2)(x - 1, y));
    float4 p21 = read_imagef(in, sampler, (int2)(x + 1, y));

    float4 p02 = read_imagef(in, sampler, (int2)(x - 1, y + 1));
    float4 p12 = read_imagef(in, sampler, (int2)(x,     y + 1));
    float4 p22 = read_imagef(in, sampler, (int2)(x + 1, y + 1));

    float3 gx = -p00.xyz + p20.xyz +
                 2.0f * (p21.xyz - p01.xyz)
                -p02.xyz + p22.xyz;

    float3 gy = -p00.xyz - p20.xyz +
                 2.0f * (p12.xyz - p10.xyz) +
                 p02.xyz + p22.xyz;

    float gs_x = 0.3333f * (gx.x + gx.y + gx.z);
    float gs_y = 0.3333f * (gy.x + gy.y + gy.z);

    float mag_g = native_sqrt(gs_x * gs_x + gs_y * gs_y);
    write_imagef(out, (int2)(x, y), (float4)(mag_g, mag_g, mag_g, 1.0f));
}
