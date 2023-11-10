class Student:

    def __init__(self, the_id: int = 0, the_name: str = '', department: str = '', stage: str = '', the_type: str = '',
                 image=None,
                 isvalid: bool = True):
        self._name = the_name
        self._stage = stage
        self._department = department
        self._type = the_type
        self._id = the_id
        self._image = image
        self._isvalid = isvalid

    def set_name(self, name):
        self._name = name

    def set_stage(self, stage):
        self._stage = stage

    def set_department(self, department):
        self._department = department

    def set_type(self, the_type):
        self._type = the_type

    def set_id(self, the_id):
        self._id = the_id

    def set_image(self, image):
        self._image = image

    def set_isvalid(self, isvalid):
        self._isvalid = isvalid

    def get_name(self):
        return self._name

    def get_stage(self):
        return self._stage

    def get_department(self):
        return self._department

    def get_type(self):
        return self._type

    def get_id(self):
        return self._id

    def get_image(self):
        return self._image

    def get_isvalid(self):
        return self._isvalid
