# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_examplecomponents')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_examplecomponents')
    _examplecomponents = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_examplecomponents', [dirname(__file__)])
        except ImportError:
            import _examplecomponents
            return _examplecomponents
        try:
            _mod = imp.load_module('_examplecomponents', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _examplecomponents = swig_import_helper()
    del swig_import_helper
else:
    import _examplecomponents
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

try:
    import weakref
    weakref_proxy = weakref.proxy
except __builtin__.Exception:
    weakref_proxy = lambda x: x


import opensim.actuators
import opensim.simulation
import opensim.common
import opensim.simbody
class ToyReflexController(opensim.simulation.Controller):
    """Proxy of C++ OpenSim::ToyReflexController class."""

    __swig_setmethods__ = {}
    for _s in [opensim.simulation.Controller]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ToyReflexController, name, value)
    __swig_getmethods__ = {}
    for _s in [opensim.simulation.Controller]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ToyReflexController, name)
    __repr__ = _swig_repr

    def safeDownCast(obj):
        """
        safeDownCast(OpenSimObject obj) -> ToyReflexController

        Parameters
        ----------
        obj: OpenSim::Object *

        """
        return _examplecomponents.ToyReflexController_safeDownCast(obj)

    safeDownCast = staticmethod(safeDownCast)

    def assign(self, aObject):
        """
        assign(ToyReflexController self, OpenSimObject aObject)

        Parameters
        ----------
        aObject: OpenSim::Object &

        """
        return _examplecomponents.ToyReflexController_assign(self, aObject)


    def getClassName():
        """getClassName() -> std::string const &"""
        return _examplecomponents.ToyReflexController_getClassName()

    getClassName = staticmethod(getClassName)

    def clone(self):
        """
        clone(ToyReflexController self) -> ToyReflexController

        Parameters
        ----------
        self: OpenSim::ToyReflexController const *

        """
        return _examplecomponents.ToyReflexController_clone(self)


    def getConcreteClassName(self):
        """
        getConcreteClassName(ToyReflexController self) -> std::string const &

        Parameters
        ----------
        self: OpenSim::ToyReflexController const *

        """
        return _examplecomponents.ToyReflexController_getConcreteClassName(self)


    def copyProperty_gain(self, source):
        """
        copyProperty_gain(ToyReflexController self, ToyReflexController source)

        Parameters
        ----------
        source: OpenSim::ToyReflexController::Self const &

        """
        return _examplecomponents.ToyReflexController_copyProperty_gain(self, source)


    def append_gain(self, value):
        """
        append_gain(ToyReflexController self, double const & value) -> int

        Parameters
        ----------
        value: double const &

        """
        return _examplecomponents.ToyReflexController_append_gain(self, value)


    def constructProperty_gain(self, initValue):
        """
        constructProperty_gain(ToyReflexController self, double const & initValue)

        Parameters
        ----------
        initValue: double const &

        """
        return _examplecomponents.ToyReflexController_constructProperty_gain(self, initValue)


    def get_gain(self, *args):
        """
        get_gain(ToyReflexController self, int i) -> double const

        Parameters
        ----------
        i: int

        get_gain(ToyReflexController self) -> double const &

        Parameters
        ----------
        self: OpenSim::ToyReflexController const *

        """
        return _examplecomponents.ToyReflexController_get_gain(self, *args)


    def upd_gain(self, *args):
        """
        upd_gain(ToyReflexController self, int i) -> double

        Parameters
        ----------
        i: int

        upd_gain(ToyReflexController self) -> double &

        Parameters
        ----------
        self: OpenSim::ToyReflexController *

        """
        return _examplecomponents.ToyReflexController_upd_gain(self, *args)


    def set_gain(self, *args):
        """
        set_gain(ToyReflexController self, int i, double const & value)

        Parameters
        ----------
        i: int
        value: double const &

        set_gain(ToyReflexController self, double const & value)

        Parameters
        ----------
        value: double const &

        """
        return _examplecomponents.ToyReflexController_set_gain(self, *args)


    def __init__(self, *args):
        """
        __init__(OpenSim::ToyReflexController self) -> ToyReflexController
        __init__(OpenSim::ToyReflexController self, double gain) -> ToyReflexController

        Parameters
        ----------
        gain: double

        """
        this = _examplecomponents.new_ToyReflexController(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def computeControls(self, s, controls):
        """
        computeControls(ToyReflexController self, State s, Vector controls)

        Parameters
        ----------
        s: SimTK::State const &
        controls: SimTK::Vector &

        """
        return _examplecomponents.ToyReflexController_computeControls(self, s, controls)

    __swig_destroy__ = _examplecomponents.delete_ToyReflexController
    __del__ = lambda self: None
ToyReflexController_swigregister = _examplecomponents.ToyReflexController_swigregister
ToyReflexController_swigregister(ToyReflexController)

def ToyReflexController_safeDownCast(obj):
    """
    ToyReflexController_safeDownCast(OpenSimObject obj) -> ToyReflexController

    Parameters
    ----------
    obj: OpenSim::Object *

    """
    return _examplecomponents.ToyReflexController_safeDownCast(obj)

def ToyReflexController_getClassName():
    """ToyReflexController_getClassName() -> std::string const &"""
    return _examplecomponents.ToyReflexController_getClassName()

class ToyPropMyoController(opensim.simulation.Controller):
    """Proxy of C++ OpenSim::ToyPropMyoController class."""

    __swig_setmethods__ = {}
    for _s in [opensim.simulation.Controller]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, ToyPropMyoController, name, value)
    __swig_getmethods__ = {}
    for _s in [opensim.simulation.Controller]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, ToyPropMyoController, name)
    __repr__ = _swig_repr

    def safeDownCast(obj):
        """
        safeDownCast(OpenSimObject obj) -> ToyPropMyoController

        Parameters
        ----------
        obj: OpenSim::Object *

        """
        return _examplecomponents.ToyPropMyoController_safeDownCast(obj)

    safeDownCast = staticmethod(safeDownCast)

    def assign(self, aObject):
        """
        assign(ToyPropMyoController self, OpenSimObject aObject)

        Parameters
        ----------
        aObject: OpenSim::Object &

        """
        return _examplecomponents.ToyPropMyoController_assign(self, aObject)


    def getClassName():
        """getClassName() -> std::string const &"""
        return _examplecomponents.ToyPropMyoController_getClassName()

    getClassName = staticmethod(getClassName)

    def clone(self):
        """
        clone(ToyPropMyoController self) -> ToyPropMyoController

        Parameters
        ----------
        self: OpenSim::ToyPropMyoController const *

        """
        return _examplecomponents.ToyPropMyoController_clone(self)


    def getConcreteClassName(self):
        """
        getConcreteClassName(ToyPropMyoController self) -> std::string const &

        Parameters
        ----------
        self: OpenSim::ToyPropMyoController const *

        """
        return _examplecomponents.ToyPropMyoController_getConcreteClassName(self)


    def copyProperty_gain(self, source):
        """
        copyProperty_gain(ToyPropMyoController self, ToyPropMyoController source)

        Parameters
        ----------
        source: OpenSim::ToyPropMyoController::Self const &

        """
        return _examplecomponents.ToyPropMyoController_copyProperty_gain(self, source)


    def append_gain(self, value):
        """
        append_gain(ToyPropMyoController self, double const & value) -> int

        Parameters
        ----------
        value: double const &

        """
        return _examplecomponents.ToyPropMyoController_append_gain(self, value)


    def constructProperty_gain(self, initValue):
        """
        constructProperty_gain(ToyPropMyoController self, double const & initValue)

        Parameters
        ----------
        initValue: double const &

        """
        return _examplecomponents.ToyPropMyoController_constructProperty_gain(self, initValue)


    def get_gain(self, *args):
        """
        get_gain(ToyPropMyoController self, int i) -> double const

        Parameters
        ----------
        i: int

        get_gain(ToyPropMyoController self) -> double const &

        Parameters
        ----------
        self: OpenSim::ToyPropMyoController const *

        """
        return _examplecomponents.ToyPropMyoController_get_gain(self, *args)


    def upd_gain(self, *args):
        """
        upd_gain(ToyPropMyoController self, int i) -> double

        Parameters
        ----------
        i: int

        upd_gain(ToyPropMyoController self) -> double &

        Parameters
        ----------
        self: OpenSim::ToyPropMyoController *

        """
        return _examplecomponents.ToyPropMyoController_upd_gain(self, *args)


    def set_gain(self, *args):
        """
        set_gain(ToyPropMyoController self, int i, double const & value)

        Parameters
        ----------
        i: int
        value: double const &

        set_gain(ToyPropMyoController self, double const & value)

        Parameters
        ----------
        value: double const &

        """
        return _examplecomponents.ToyPropMyoController_set_gain(self, *args)

    __swig_setmethods__["PropertyIndex_socket_actuator"] = _examplecomponents.ToyPropMyoController_PropertyIndex_socket_actuator_set
    __swig_getmethods__["PropertyIndex_socket_actuator"] = _examplecomponents.ToyPropMyoController_PropertyIndex_socket_actuator_get
    if _newclass:
        PropertyIndex_socket_actuator = _swig_property(_examplecomponents.ToyPropMyoController_PropertyIndex_socket_actuator_get, _examplecomponents.ToyPropMyoController_PropertyIndex_socket_actuator_set)

    def connectSocket_actuator(self, object):
        """
        connectSocket_actuator(ToyPropMyoController self, OpenSimObject object)

        Parameters
        ----------
        object: OpenSim::Object const &

        """
        return _examplecomponents.ToyPropMyoController_connectSocket_actuator(self, object)

    __swig_setmethods__["PropertyIndex_input_activation"] = _examplecomponents.ToyPropMyoController_PropertyIndex_input_activation_set
    __swig_getmethods__["PropertyIndex_input_activation"] = _examplecomponents.ToyPropMyoController_PropertyIndex_input_activation_get
    if _newclass:
        PropertyIndex_input_activation = _swig_property(_examplecomponents.ToyPropMyoController_PropertyIndex_input_activation_get, _examplecomponents.ToyPropMyoController_PropertyIndex_input_activation_set)

    def connectInput_activation(self, *args):
        """
        connectInput_activation(ToyPropMyoController self, AbstractOutput output, std::string const & alias)

        Parameters
        ----------
        output: OpenSim::AbstractOutput const &
        alias: std::string const &

        connectInput_activation(ToyPropMyoController self, AbstractOutput output)

        Parameters
        ----------
        output: OpenSim::AbstractOutput const &

        connectInput_activation(ToyPropMyoController self, AbstractChannel channel, std::string const & alias)

        Parameters
        ----------
        channel: OpenSim::AbstractChannel const &
        alias: std::string const &

        connectInput_activation(ToyPropMyoController self, AbstractChannel channel)

        Parameters
        ----------
        channel: OpenSim::AbstractChannel const &

        """
        return _examplecomponents.ToyPropMyoController_connectInput_activation(self, *args)

    __swig_setmethods__["_has_output_myo_control"] = _examplecomponents.ToyPropMyoController__has_output_myo_control_set
    __swig_getmethods__["_has_output_myo_control"] = _examplecomponents.ToyPropMyoController__has_output_myo_control_get
    if _newclass:
        _has_output_myo_control = _swig_property(_examplecomponents.ToyPropMyoController__has_output_myo_control_get, _examplecomponents.ToyPropMyoController__has_output_myo_control_set)

    def __init__(self):
        """__init__(OpenSim::ToyPropMyoController self) -> ToyPropMyoController"""
        this = _examplecomponents.new_ToyPropMyoController()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def computeControl(self, s):
        """
        computeControl(ToyPropMyoController self, State s) -> double

        Parameters
        ----------
        s: SimTK::State const &

        """
        return _examplecomponents.ToyPropMyoController_computeControl(self, s)


    def computeControls(self, s, controls):
        """
        computeControls(ToyPropMyoController self, State s, Vector controls)

        Parameters
        ----------
        s: SimTK::State const &
        controls: SimTK::Vector &

        """
        return _examplecomponents.ToyPropMyoController_computeControls(self, s, controls)

    __swig_destroy__ = _examplecomponents.delete_ToyPropMyoController
    __del__ = lambda self: None
ToyPropMyoController_swigregister = _examplecomponents.ToyPropMyoController_swigregister
ToyPropMyoController_swigregister(ToyPropMyoController)

def ToyPropMyoController_safeDownCast(obj):
    """
    ToyPropMyoController_safeDownCast(OpenSimObject obj) -> ToyPropMyoController

    Parameters
    ----------
    obj: OpenSim::Object *

    """
    return _examplecomponents.ToyPropMyoController_safeDownCast(obj)

def ToyPropMyoController_getClassName():
    """ToyPropMyoController_getClassName() -> std::string const &"""
    return _examplecomponents.ToyPropMyoController_getClassName()

class HopperDevice(opensim.simulation.ModelComponent):
    """Proxy of C++ OpenSim::HopperDevice class."""

    __swig_setmethods__ = {}
    for _s in [opensim.simulation.ModelComponent]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, HopperDevice, name, value)
    __swig_getmethods__ = {}
    for _s in [opensim.simulation.ModelComponent]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, HopperDevice, name)
    __repr__ = _swig_repr

    def safeDownCast(obj):
        """
        safeDownCast(OpenSimObject obj) -> HopperDevice

        Parameters
        ----------
        obj: OpenSim::Object *

        """
        return _examplecomponents.HopperDevice_safeDownCast(obj)

    safeDownCast = staticmethod(safeDownCast)

    def assign(self, aObject):
        """
        assign(HopperDevice self, OpenSimObject aObject)

        Parameters
        ----------
        aObject: OpenSim::Object &

        """
        return _examplecomponents.HopperDevice_assign(self, aObject)


    def getClassName():
        """getClassName() -> std::string const &"""
        return _examplecomponents.HopperDevice_getClassName()

    getClassName = staticmethod(getClassName)

    def clone(self):
        """
        clone(HopperDevice self) -> HopperDevice

        Parameters
        ----------
        self: OpenSim::HopperDevice const *

        """
        return _examplecomponents.HopperDevice_clone(self)


    def getConcreteClassName(self):
        """
        getConcreteClassName(HopperDevice self) -> std::string const &

        Parameters
        ----------
        self: OpenSim::HopperDevice const *

        """
        return _examplecomponents.HopperDevice_getConcreteClassName(self)

    __swig_setmethods__["_has_output_length"] = _examplecomponents.HopperDevice__has_output_length_set
    __swig_getmethods__["_has_output_length"] = _examplecomponents.HopperDevice__has_output_length_get
    if _newclass:
        _has_output_length = _swig_property(_examplecomponents.HopperDevice__has_output_length_get, _examplecomponents.HopperDevice__has_output_length_set)
    __swig_setmethods__["_has_output_speed"] = _examplecomponents.HopperDevice__has_output_speed_set
    __swig_getmethods__["_has_output_speed"] = _examplecomponents.HopperDevice__has_output_speed_get
    if _newclass:
        _has_output_speed = _swig_property(_examplecomponents.HopperDevice__has_output_speed_get, _examplecomponents.HopperDevice__has_output_speed_set)
    __swig_setmethods__["_has_output_tension"] = _examplecomponents.HopperDevice__has_output_tension_set
    __swig_getmethods__["_has_output_tension"] = _examplecomponents.HopperDevice__has_output_tension_get
    if _newclass:
        _has_output_tension = _swig_property(_examplecomponents.HopperDevice__has_output_tension_get, _examplecomponents.HopperDevice__has_output_tension_set)
    __swig_setmethods__["_has_output_power"] = _examplecomponents.HopperDevice__has_output_power_set
    __swig_getmethods__["_has_output_power"] = _examplecomponents.HopperDevice__has_output_power_get
    if _newclass:
        _has_output_power = _swig_property(_examplecomponents.HopperDevice__has_output_power_get, _examplecomponents.HopperDevice__has_output_power_set)
    __swig_setmethods__["_has_output_height"] = _examplecomponents.HopperDevice__has_output_height_set
    __swig_getmethods__["_has_output_height"] = _examplecomponents.HopperDevice__has_output_height_get
    if _newclass:
        _has_output_height = _swig_property(_examplecomponents.HopperDevice__has_output_height_get, _examplecomponents.HopperDevice__has_output_height_set)
    __swig_setmethods__["_has_output_com_height"] = _examplecomponents.HopperDevice__has_output_com_height_set
    __swig_getmethods__["_has_output_com_height"] = _examplecomponents.HopperDevice__has_output_com_height_get
    if _newclass:
        _has_output_com_height = _swig_property(_examplecomponents.HopperDevice__has_output_com_height_get, _examplecomponents.HopperDevice__has_output_com_height_set)

    def copyProperty_actuator_name(self, source):
        """
        copyProperty_actuator_name(HopperDevice self, HopperDevice source)

        Parameters
        ----------
        source: OpenSim::HopperDevice::Self const &

        """
        return _examplecomponents.HopperDevice_copyProperty_actuator_name(self, source)


    def append_actuator_name(self, value):
        """
        append_actuator_name(HopperDevice self, std::string const & value) -> int

        Parameters
        ----------
        value: std::string const &

        """
        return _examplecomponents.HopperDevice_append_actuator_name(self, value)


    def constructProperty_actuator_name(self, initValue):
        """
        constructProperty_actuator_name(HopperDevice self, std::string const & initValue)

        Parameters
        ----------
        initValue: std::string const &

        """
        return _examplecomponents.HopperDevice_constructProperty_actuator_name(self, initValue)


    def get_actuator_name(self, *args):
        """
        get_actuator_name(HopperDevice self, int i) -> std::string const

        Parameters
        ----------
        i: int

        get_actuator_name(HopperDevice self) -> std::string const &

        Parameters
        ----------
        self: OpenSim::HopperDevice const *

        """
        return _examplecomponents.HopperDevice_get_actuator_name(self, *args)


    def upd_actuator_name(self, *args):
        """
        upd_actuator_name(HopperDevice self, int i) -> std::string

        Parameters
        ----------
        i: int

        upd_actuator_name(HopperDevice self) -> std::string &

        Parameters
        ----------
        self: OpenSim::HopperDevice *

        """
        return _examplecomponents.HopperDevice_upd_actuator_name(self, *args)


    def set_actuator_name(self, *args):
        """
        set_actuator_name(HopperDevice self, int i, std::string const & value)

        Parameters
        ----------
        i: int
        value: std::string const &

        set_actuator_name(HopperDevice self, std::string const & value)

        Parameters
        ----------
        value: std::string const &

        """
        return _examplecomponents.HopperDevice_set_actuator_name(self, *args)


    def __init__(self):
        """__init__(OpenSim::HopperDevice self) -> HopperDevice"""
        this = _examplecomponents.new_HopperDevice()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def getLength(self, s):
        """
        getLength(HopperDevice self, State s) -> double

        Parameters
        ----------
        s: SimTK::State const &

        """
        return _examplecomponents.HopperDevice_getLength(self, s)


    def getSpeed(self, s):
        """
        getSpeed(HopperDevice self, State s) -> double

        Parameters
        ----------
        s: SimTK::State const &

        """
        return _examplecomponents.HopperDevice_getSpeed(self, s)


    def getTension(self, s):
        """
        getTension(HopperDevice self, State s) -> double

        Parameters
        ----------
        s: SimTK::State const &

        """
        return _examplecomponents.HopperDevice_getTension(self, s)


    def getPower(self, s):
        """
        getPower(HopperDevice self, State s) -> double

        Parameters
        ----------
        s: SimTK::State const &

        """
        return _examplecomponents.HopperDevice_getPower(self, s)


    def getHeight(self, s):
        """
        getHeight(HopperDevice self, State s) -> double

        Parameters
        ----------
        s: SimTK::State const &

        """
        return _examplecomponents.HopperDevice_getHeight(self, s)


    def getCenterOfMassHeight(self, s):
        """
        getCenterOfMassHeight(HopperDevice self, State s) -> double

        Parameters
        ----------
        s: SimTK::State const &

        """
        return _examplecomponents.HopperDevice_getCenterOfMassHeight(self, s)

    __swig_destroy__ = _examplecomponents.delete_HopperDevice
    __del__ = lambda self: None
HopperDevice_swigregister = _examplecomponents.HopperDevice_swigregister
HopperDevice_swigregister(HopperDevice)

def HopperDevice_safeDownCast(obj):
    """
    HopperDevice_safeDownCast(OpenSimObject obj) -> HopperDevice

    Parameters
    ----------
    obj: OpenSim::Object *

    """
    return _examplecomponents.HopperDevice_safeDownCast(obj)

def HopperDevice_getClassName():
    """HopperDevice_getClassName() -> std::string const &"""
    return _examplecomponents.HopperDevice_getClassName()

# This file is compatible with both classic and new-style classes.

