from www.models import Device

class DeviceRepository():
    def get_all_devices(self):
        return Device.objects.all()

    def get_by_pk(self, pk):
        return Device.objects.get(pk=pk)

    def get_free_devices(self):
        return Device.filter(reserved_by=None)
