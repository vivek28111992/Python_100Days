class SetOnceMappingMixin:
  """Custom mixin class"""
  __slots__ = ()

  def __setitem__(self, key, value):
    if key in self:
      raise KeyError(str(key) + 'already set')
    return super().__setitem__(key, value)

class SetOnceDict(SetOnceMappingMixin, dict):
  """Custom Dictionary"""
  pass

my_dict = SetOnceDict()
try:
  my_dict['username'] = 'jackfrued'
  my_dict['username'] = 'hellokitty'
except KeyError:
  pass
print(my_dict)
