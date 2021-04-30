import abc

class Filter(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def applyFilter(self, ls_all):
        pass
    