

_SceneLighting_001_parameters = {
    'IN' : {},
    'OUT' : {},
}
_SceneLighting_001_parameters["IN"]["Scene"] = IN["Scene"]
_SceneLighting_001_parameters["IN"]["Point Resolution"] = PARAMETERS["_SceneLighting_001"]["Point Resolution"]
_SceneLighting_001_parameters["IN"]["Spot Resolution"] = PARAMETERS["_SceneLighting_001"]["Spot Resolution"]
_SceneLighting_001_parameters["IN"]["Sun Resolution"] = PARAMETERS["_SceneLighting_001"]["Sun Resolution"]
_SceneLighting_001_parameters["IN"]["Sun Max Distance"] = PARAMETERS["_SceneLighting_001"]["Sun Max Distance"]
_SceneLighting_001_parameters["IN"]["Sun CSM Count"] = PARAMETERS["_SceneLighting_001"]["Sun CSM Count"]
_SceneLighting_001_parameters["IN"]["Sun CSM Distribution"] = PARAMETERS["_SceneLighting_001"]["Sun CSM Distribution"]
_SceneLighting_001_parameters["OUT"]["Scene"] = None
run_node("_SceneLighting_001", "SceneLighting", _SceneLighting_001_parameters)


_RenderLayers_parameters = {
    'IN' : {},
    'OUT' : {},
}
_RenderLayers_parameters["IN"]["Scene"] = _SceneLighting_001_parameters["OUT"]["Scene"]
_RenderLayers_parameters["IN"]["Transparent Layers"] = PARAMETERS["_RenderLayers"]["Transparent Layers"]
_RenderLayers_parameters["OUT"]["Color"] = None
_RenderLayers_parameters["PASS_GRAPH"] = PARAMETERS["_RenderLayers"]["PASS_GRAPH"]
_RenderLayers_parameters["CUSTOM_IO"] = PARAMETERS["_RenderLayers"]["CUSTOM_IO"]
run_node("_RenderLayers", "RenderLayers", _RenderLayers_parameters)


_ScreenPass_parameters = {
    'IN' : {},
    'OUT' : {},
}
_ScreenPass_parameters["IN"]["Color"] = _RenderLayers_parameters["OUT"]["Color"]
_ScreenPass_parameters["OUT"]["Color"] = None
_ScreenPass_parameters["PASS_MATERIAL"] = PARAMETERS["_ScreenPass"]["PASS_MATERIAL"]
_ScreenPass_parameters["CUSTOM_IO"] = PARAMETERS["_ScreenPass"]["CUSTOM_IO"]
run_node("_ScreenPass", "ScreenPass", _ScreenPass_parameters)


_SuperSamplingAA_parameters = {
    'IN' : {},
    'OUT' : {},
}
_SuperSamplingAA_parameters["IN"]["Color"] = _ScreenPass_parameters["OUT"]["Color"]
_SuperSamplingAA_parameters["OUT"]["Color"] = None
run_node("_SuperSamplingAA", "SuperSamplingAA", _SuperSamplingAA_parameters)

OUT["Color"] = _SuperSamplingAA_parameters["OUT"]["Color"]
OUT["Depth"] = PARAMETERS["_Render_Output"]["Depth"]
