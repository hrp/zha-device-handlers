"""Echostar Bell Device"""
"""Sage Doorbell Sensor Device"""

from zigpy.profiles import zha
from zigpy.quirks import CustomDevice
from zigpy.zcl.clusters.general import (
    Basic,
    Identify, 
    Alarms, 
    OnOff, 
    LevelControl, 
    Ota,
)

from ..const import (
    DEVICE_TYPE,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PROFILE_ID,
)

MANUFACTURER = " Echostar"
MODEL = "  Bell"

class Bell(CustomDevice):
    """Echostar Bell device"""

    signature = {
        # <SimpleDescriptor endpoint=18 profile=260 device_type=260 
        # device_version=0 
        # input_clusters=[0, 3, 9, 1] 
        # output_clusters=[3, 6, 8, 25]>
        MODELS_INFO: [(MANUFACTURER, MODEL)],
        ENDPOINTS: {
            18: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.DIMMER_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Alarms.cluster_id,
                    PowerConfiguration.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                ],
            }
        },
    }

    replacement = {
        ENDPOINTS: {
            18: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_SWITCH,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Alarms.cluster_id,
                    PowerConfiguration.cluster_id,
                ],
                OUTPUT_CLUSTERS: [
                    Identify.cluster_id,
                    OnOff.cluster_id,
                    LevelControl.cluster_id,
                    Ota.cluster_id,
                ],
            }
        },
    }

