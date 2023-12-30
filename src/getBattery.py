from pymobiledevice3.lockdown import LockdownClient
from pymobiledevice3.services.diagnostics import DiagnosticsService
from pymobiledevice3.remote.remote_service_discovery import RemoteServiceDiscoveryService
from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.services.syslog import SyslogService
from pymobiledevice3.cli.cli_common import Command, print_json
import json

lockdown = create_using_usbmux()

def default_json_encoder(obj):
    if isinstance(obj, bytes):
        return f'<{obj.hex()}>'
    if isinstance(obj, datetime.datetime):
        return str(obj)
    if isinstance(obj, uuid.UUID):
        return str(obj)
    raise TypeError()

def diagnostics_battery_single(service_provider: LockdownClient):
    """ get single snapshot of battery data """

    raw_info = DiagnosticsService(lockdown=service_provider).get_battery()

    custom = {
        'InstantAmperage': raw_info.get('InstantAmperage'),
        'Temperature': raw_info.get('Temperature'),
        'Voltage': raw_info.get('Voltage'),
        'IsCharging': raw_info.get('IsCharging'),
        'CurrentCapacity': raw_info.get('CurrentCapacity'),
        'AbsoluteCapacity': raw_info.get('AbsoluteCapacity'),
        'AdapterDetails': raw_info.get('AdapterDetails'),
        'AdapterInfo': raw_info.get('AdapterInfo'),
        'Amperage': raw_info.get('Amperage'),
        'AppleRawAdapterDetails': raw_info.get('AppleRawAdapterDetails'),
        'AppleRawBatteryVoltage': raw_info.get('AppleRawBatteryVoltage'),
        "AppleRawBatteryVoltage": 4456,
        'AppleRawCurrentCapacity': raw_info.get('AppleRawCurrentCapacity'),
        'AppleRawExternalConnected': raw_info.get('AppleRawExternalConnected'),
        'AppleRawMaxCapacity': raw_info.get('AppleRawMaxCapacity'),
        'AtCriticalLevel': raw_info.get('AtCriticalLevel'),
        'AvgTimeToEmpty': raw_info.get('AvgTimeToEmpty'),
        'BatteryCellDisconnectCount': raw_info.get('BatteryCellDisconnectCount'),
        'BatteryData': raw_info.get('BatteryData'),
        'BatteryInstalled': raw_info.get('BatteryInstalled'),
        'BatteryInvalidWakeSeconds': raw_info.get('BatteryInvalidWakeSeconds'),
        'BestAdapterIndex': raw_info.get('BestAdapterIndex'),
        'BootPathUpdated': raw_info.get('BootPathUpdated'),
        'BootVoltage': raw_info.get('BootVoltage'),
        'CarrierMode': raw_info.get('CarrierMode'),
        'ChargerConfiguration': raw_info.get('ChargerConfiguration'),
        'ChargerData': raw_info.get('ChargerData'),
        'ChargingOverride': raw_info.get('ChargingOverride'),
        'CycleCount': raw_info.get('CycleCount'),
        'DeadBatteryBootData': raw_info.get('DeadBatteryBootData'),
        'DesignCapacity': raw_info.get('DesignCapacity'),
        'ExternalChargeCapable': raw_info.get('ExternalChargeCapable'),
        'ExternalConnected': raw_info.get('ExternalConnected'),
        'FedDetails': raw_info.get('FedDetails'),
        'FullPathUpdated': raw_info.get('FullPathUpdated'),
        'FullyCharged': raw_info.get('FullyCharged'),
        'GasGaugeFirmwareVersion': raw_info.get('GasGaugeFirmwareVersion'),
        'IOGeneralInterest': raw_info.get('IOGeneralInterest'),
        'IOReportLegend': raw_info.get('IOReportLegend'),
        'IOReportLegendPublic': raw_info.get('IOReportLegendPublic'),
        'InductiveData': raw_info.get('InductiveData'),
        'IsCharging': raw_info.get('IsCharging'),
        'KioskMode': raw_info.get('KioskMode'),
        'LPEMData': raw_info.get('LPEMData'),
        'Location': raw_info.get('Location'),
        'ManufacturerData': raw_info.get('ManufacturerData'),
        'MaxCapacity': raw_info.get('MaxCapacity'),
        'NominalChargeCapacity': raw_info.get('NominalChargeCapacity'),
        'PortControllerInfo': raw_info.get('PortControllerInfo'),
        'Serial': raw_info.get('Serial'),
        'PostChargeWaitSeconds': raw_info.get('PostChargeWaitSeconds'),
        'PostDischargeWaitSeconds': raw_info.get('PostDischargeWaitSeconds'),
        'PowerTelemetryData': raw_info.get('PowerTelemetryData'),
        'Temperature': raw_info.get('Temperature'),
        'TimeRemaining': raw_info.get('TimeRemaining'),
        'UpdateTime': raw_info.get('UpdateTime'),
        'UserVisiblePathUpdated': raw_info.get('UserVisiblePathUpdated'),
        'VirtualTemperature': raw_info.get('VirtualTemperature'),
        'Voltage': raw_info.get('Voltage'),
        'built-in': raw_info.get('built-in'),
    }

    ' Stringify '
    customString = json.dumps(custom, sort_keys=True, default=default_json_encoder)

    ' Get current path '


    f = open("src/battery.json", "w")
    f.write(customString)
    f.close()
    

    



diagnostics_battery_single(lockdown)

