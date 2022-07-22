


#include "NPR_ScreenShader.glsl"
#include "Node Utils/node_utils.glsl"




layout (location = 0) out vec4 OUT_SCREEN_SHADER_COLOR;
uniform vec4 U_0_Background_0_v;
uniform sampler2D IN_SCREEN_SHADER_COLOR;


#ifdef PIXEL_SHADER
void SCREEN_SHADER()
{
	vec4 _Background_0_result = vec4_color_property(U_0_Background_0_v);


	vec2 _screen_uv_0_result = screen_uv();

	vec4 _sampler2D_sample_0_result = sampler2D_sample(IN_SCREEN_SHADER_COLOR,_screen_uv_0_result);

	vec4 _alpha_blend_0_result = alpha_blend(_Background_0_result,_sampler2D_sample_0_result);

	OUT_SCREEN_SHADER_COLOR = _alpha_blend_0_result;

}
#endif //PIXEL_SHADER


