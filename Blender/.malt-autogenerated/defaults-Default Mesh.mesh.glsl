


#include "NPR_MeshShader.glsl"
#include "Node Utils/node_utils.glsl"




uniform vec4 U_0_MAIN_PASS_PIXEL_SHADER_Output_0_Line_Color;
uniform float U_0_MAIN_PASS_PIXEL_SHADER_Output_0_Line_Width;
#ifdef MAIN_PASS
layout (location = 0) out vec4 OUT_MAIN_PASS_PIXEL_SHADER_COLOR;
layout (location = 1) out vec4 OUT_MAIN_PASS_PIXEL_SHADER_LINECOLOR;
layout (location = 2) out float OUT_MAIN_PASS_PIXEL_SHADER_LINEWIDTH;
#endif //MAIN_PASS
uniform vec3 U_0_diffuse_half_shading_0_position;
uniform vec3 U_0_diffuse_half_shading_0_normal;
uniform int U_0_diffuse_half_shading_0_light_group;
uniform bool U_0_diffuse_half_shading_0_shadows;
uniform bool U_0_diffuse_half_shading_0_self_shadows;


#ifdef PIXEL_SHADER
void MAIN_PASS_PIXEL_SHADER()
{
	vec3 _diffuse_half_shading_0_result = diffuse_half_shading(POSITION,NORMAL,U_0_diffuse_half_shading_0_light_group,U_0_diffuse_half_shading_0_shadows,U_0_diffuse_half_shading_0_self_shadows);

	#ifdef MAIN_PASS
	OUT_MAIN_PASS_PIXEL_SHADER_COLOR = vec4_from_vec3(_diffuse_half_shading_0_result);
	OUT_MAIN_PASS_PIXEL_SHADER_LINECOLOR = U_0_MAIN_PASS_PIXEL_SHADER_Output_0_Line_Color;
	OUT_MAIN_PASS_PIXEL_SHADER_LINEWIDTH = U_0_MAIN_PASS_PIXEL_SHADER_Output_0_Line_Width;
	#endif //MAIN_PASS

}
#endif //PIXEL_SHADER


