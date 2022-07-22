

_PrePass_parameters = {
    'IN' : {},
    'OUT' : {},
}
_PrePass_parameters["IN"]["Scene"] = IN["Scene"]
_PrePass_parameters["OUT"]["Scene"] = None
_PrePass_parameters["OUT"]["Normal Depth"] = None
_PrePass_parameters["OUT"]["ID"] = None
_PrePass_parameters["CUSTOM_IO"] = PARAMETERS["_PrePass"]["CUSTOM_IO"]
run_node("_PrePass", "PrePass", _PrePass_parameters)


_MainPass_parameters = {
    'IN' : {},
    'OUT' : {},
}
_MainPass_parameters["IN"]["Scene"] = _PrePass_parameters["OUT"]["Scene"]
_MainPass_parameters["IN"]["Normal Depth"] = PARAMETERS["_MainPass"]["Normal Depth"]
_MainPass_parameters["IN"]["ID"] = PARAMETERS["_MainPass"]["ID"]
_MainPass_parameters["OUT"]["Color"] = None
_MainPass_parameters["OUT"]["Line Color"] = None
_MainPass_parameters["OUT"]["Line Width"] = None
_MainPass_parameters["CUSTOM_IO"] = PARAMETERS["_MainPass"]["CUSTOM_IO"]
run_node("_MainPass", "MainPass", _MainPass_parameters)


_LineRender_parameters = {
    'IN' : {},
    'OUT' : {},
}
_LineRender_parameters["IN"]["Color"] = _MainPass_parameters["OUT"]["Color"]
_LineRender_parameters["IN"]["Line Color"] = _MainPass_parameters["OUT"]["Line Color"]
_LineRender_parameters["IN"]["Line Width"] = _MainPass_parameters["OUT"]["Line Width"]
_LineRender_parameters["IN"]["Max Width"] = PARAMETERS["_LineRender"]["Max Width"]
_LineRender_parameters["IN"]["Line Scale"] = PARAMETERS["_LineRender"]["Line Scale"]
_LineRender_parameters["IN"]["Normal Depth"] = _PrePass_parameters["OUT"]["Normal Depth"]
_LineRender_parameters["IN"]["ID"] = _PrePass_parameters["OUT"]["ID"]
_LineRender_parameters["OUT"]["Color"] = None
run_node("_LineRender", "LineRender", _LineRender_parameters)

OUT["Color"] = _LineRender_parameters["OUT"]["Color"]
