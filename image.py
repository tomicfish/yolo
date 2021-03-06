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
        mname = '.'.join((pkg, '_image')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_image')
    _image = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_image', [dirname(__file__)])
        except ImportError:
            import _image
            return _image
        try:
            _mod = imp.load_module('_image', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _image = swig_import_helper()
    del swig_import_helper
else:
    import _image
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

class image(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, image, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, image, name)
    __repr__ = _swig_repr
    __swig_setmethods__["h"] = _image.image_h_set
    __swig_getmethods__["h"] = _image.image_h_get
    if _newclass:
        h = _swig_property(_image.image_h_get, _image.image_h_set)
    __swig_setmethods__["w"] = _image.image_w_set
    __swig_getmethods__["w"] = _image.image_w_get
    if _newclass:
        w = _swig_property(_image.image_w_get, _image.image_w_set)
    __swig_setmethods__["c"] = _image.image_c_set
    __swig_getmethods__["c"] = _image.image_c_get
    if _newclass:
        c = _swig_property(_image.image_c_get, _image.image_c_set)
    __swig_setmethods__["data"] = _image.image_data_set
    __swig_getmethods__["data"] = _image.image_data_get
    if _newclass:
        data = _swig_property(_image.image_data_get, _image.image_data_set)

    def __init__(self):
        this = _image.new_image()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _image.delete_image
    __del__ = lambda self: None
image_swigregister = _image.image_swigregister
image_swigregister(image)


def get_color(c, x, max):
    return _image.get_color(c, x, max)
get_color = _image.get_color

def flip_image(a):
    return _image.flip_image(a)
flip_image = _image.flip_image

def draw_box(a, x1, y1, x2, y2, r, g, b):
    return _image.draw_box(a, x1, y1, x2, y2, r, g, b)
draw_box = _image.draw_box

def draw_box_width(a, x1, y1, x2, y2, w, r, g, b):
    return _image.draw_box_width(a, x1, y1, x2, y2, w, r, g, b)
draw_box_width = _image.draw_box_width

def draw_bbox(a, bbox, w, r, g, b):
    return _image.draw_bbox(a, bbox, w, r, g, b)
draw_bbox = _image.draw_bbox

def draw_label(a, r, c, label, rgb):
    return _image.draw_label(a, r, c, label, rgb)
draw_label = _image.draw_label

def draw_detections(im, num, thresh, boxes, probs, names, labels, classes):
    return _image.draw_detections(im, num, thresh, boxes, probs, names, labels, classes)
draw_detections = _image.draw_detections

def image_distance(a, b):
    return _image.image_distance(a, b)
image_distance = _image.image_distance

def scale_image(m, s):
    return _image.scale_image(m, s)
scale_image = _image.scale_image

def crop_image(im, dx, dy, w, h):
    return _image.crop_image(im, dx, dy, w, h)
crop_image = _image.crop_image

def random_crop_image(im, w, h):
    return _image.random_crop_image(im, w, h)
random_crop_image = _image.random_crop_image

def random_augment_image(im, angle, aspect, low, high, size):
    return _image.random_augment_image(im, angle, aspect, low, high, size)
random_augment_image = _image.random_augment_image

def random_distort_image(im, hue, saturation, exposure):
    return _image.random_distort_image(im, hue, saturation, exposure)
random_distort_image = _image.random_distort_image

def resize_image(im, w, h):
    return _image.resize_image(im, w, h)
resize_image = _image.resize_image

def resize_min(im, min):
    return _image.resize_min(im, min)
resize_min = _image.resize_min

def resize_max(im, max):
    return _image.resize_max(im, max)
resize_max = _image.resize_max

def translate_image(m, s):
    return _image.translate_image(m, s)
translate_image = _image.translate_image

def normalize_image(p):
    return _image.normalize_image(p)
normalize_image = _image.normalize_image

def rotate_image(m, rad):
    return _image.rotate_image(m, rad)
rotate_image = _image.rotate_image

def rotate_image_cw(im, times):
    return _image.rotate_image_cw(im, times)
rotate_image_cw = _image.rotate_image_cw

def embed_image(source, dest, dx, dy):
    return _image.embed_image(source, dest, dx, dy)
embed_image = _image.embed_image

def saturate_image(im, sat):
    return _image.saturate_image(im, sat)
saturate_image = _image.saturate_image

def exposure_image(im, sat):
    return _image.exposure_image(im, sat)
exposure_image = _image.exposure_image

def distort_image(im, hue, sat, val):
    return _image.distort_image(im, hue, sat, val)
distort_image = _image.distort_image

def saturate_exposure_image(im, sat, exposure):
    return _image.saturate_exposure_image(im, sat, exposure)
saturate_exposure_image = _image.saturate_exposure_image

def hsv_to_rgb(im):
    return _image.hsv_to_rgb(im)
hsv_to_rgb = _image.hsv_to_rgb

def rgbgr_image(im):
    return _image.rgbgr_image(im)
rgbgr_image = _image.rgbgr_image

def constrain_image(im):
    return _image.constrain_image(im)
constrain_image = _image.constrain_image

def composite_3d(f1, f2, out, delta):
    return _image.composite_3d(f1, f2, out, delta)
composite_3d = _image.composite_3d

def best_3d_shift_r(a, b, min, max):
    return _image.best_3d_shift_r(a, b, min, max)
best_3d_shift_r = _image.best_3d_shift_r

def grayscale_image(im):
    return _image.grayscale_image(im)
grayscale_image = _image.grayscale_image

def threshold_image(im, thresh):
    return _image.threshold_image(im, thresh)
threshold_image = _image.threshold_image

def collapse_image_layers(source, border):
    return _image.collapse_image_layers(source, border)
collapse_image_layers = _image.collapse_image_layers

def collapse_images_horz(ims, n):
    return _image.collapse_images_horz(ims, n)
collapse_images_horz = _image.collapse_images_horz

def collapse_images_vert(ims, n):
    return _image.collapse_images_vert(ims, n)
collapse_images_vert = _image.collapse_images_vert

def show_image(p, name):
    return _image.show_image(p, name)
show_image = _image.show_image

def show_image_normalized(im, name):
    return _image.show_image_normalized(im, name)
show_image_normalized = _image.show_image_normalized

def save_image_png(im, name):
    return _image.save_image_png(im, name)
save_image_png = _image.save_image_png

def save_image(p, name):
    return _image.save_image(p, name)
save_image = _image.save_image

def show_images(ims, n, window):
    return _image.show_images(ims, n, window)
show_images = _image.show_images

def show_image_layers(p, name):
    return _image.show_image_layers(p, name)
show_image_layers = _image.show_image_layers

def show_image_collapsed(p, name):
    return _image.show_image_collapsed(p, name)
show_image_collapsed = _image.show_image_collapsed

def print_image(m):
    return _image.print_image(m)
print_image = _image.print_image

def make_image(w, h, c):
    return _image.make_image(w, h, c)
make_image = _image.make_image

def make_random_image(w, h, c):
    return _image.make_random_image(w, h, c)
make_random_image = _image.make_random_image

def make_empty_image(w, h, c):
    return _image.make_empty_image(w, h, c)
make_empty_image = _image.make_empty_image

def float_to_image(w, h, c, data):
    return _image.float_to_image(w, h, c, data)
float_to_image = _image.float_to_image

def copy_image(p):
    return _image.copy_image(p)
copy_image = _image.copy_image

def load_image(filename, w, h, c):
    return _image.load_image(filename, w, h, c)
load_image = _image.load_image

def load_image_color(filename, w, h):
    return _image.load_image_color(filename, w, h)
load_image_color = _image.load_image_color

def load_alphabet():
    return _image.load_alphabet()
load_alphabet = _image.load_alphabet

def get_pixel(m, x, y, c):
    return _image.get_pixel(m, x, y, c)
get_pixel = _image.get_pixel

def get_pixel_extend(m, x, y, c):
    return _image.get_pixel_extend(m, x, y, c)
get_pixel_extend = _image.get_pixel_extend

def set_pixel(m, x, y, c, val):
    return _image.set_pixel(m, x, y, c, val)
set_pixel = _image.set_pixel

def add_pixel(m, x, y, c, val):
    return _image.add_pixel(m, x, y, c, val)
add_pixel = _image.add_pixel

def bilinear_interpolate(im, x, y, c):
    return _image.bilinear_interpolate(im, x, y, c)
bilinear_interpolate = _image.bilinear_interpolate

def get_image_layer(m, l):
    return _image.get_image_layer(m, l)
get_image_layer = _image.get_image_layer

def free_image(m):
    return _image.free_image(m)
free_image = _image.free_image

def test_resize(filename):
    return _image.test_resize(filename)
test_resize = _image.test_resize
class box(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, box, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, box, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _image.box_x_set
    __swig_getmethods__["x"] = _image.box_x_get
    if _newclass:
        x = _swig_property(_image.box_x_get, _image.box_x_set)
    __swig_setmethods__["y"] = _image.box_y_set
    __swig_getmethods__["y"] = _image.box_y_get
    if _newclass:
        y = _swig_property(_image.box_y_get, _image.box_y_set)
    __swig_setmethods__["w"] = _image.box_w_set
    __swig_getmethods__["w"] = _image.box_w_get
    if _newclass:
        w = _swig_property(_image.box_w_get, _image.box_w_set)
    __swig_setmethods__["h"] = _image.box_h_set
    __swig_getmethods__["h"] = _image.box_h_get
    if _newclass:
        h = _swig_property(_image.box_h_get, _image.box_h_set)

    def __init__(self):
        this = _image.new_box()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _image.delete_box
    __del__ = lambda self: None
box_swigregister = _image.box_swigregister
box_swigregister(box)

class dbox(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, dbox, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, dbox, name)
    __repr__ = _swig_repr
    __swig_setmethods__["dx"] = _image.dbox_dx_set
    __swig_getmethods__["dx"] = _image.dbox_dx_get
    if _newclass:
        dx = _swig_property(_image.dbox_dx_get, _image.dbox_dx_set)
    __swig_setmethods__["dy"] = _image.dbox_dy_set
    __swig_getmethods__["dy"] = _image.dbox_dy_get
    if _newclass:
        dy = _swig_property(_image.dbox_dy_get, _image.dbox_dy_set)
    __swig_setmethods__["dw"] = _image.dbox_dw_set
    __swig_getmethods__["dw"] = _image.dbox_dw_get
    if _newclass:
        dw = _swig_property(_image.dbox_dw_get, _image.dbox_dw_set)
    __swig_setmethods__["dh"] = _image.dbox_dh_set
    __swig_getmethods__["dh"] = _image.dbox_dh_get
    if _newclass:
        dh = _swig_property(_image.dbox_dh_get, _image.dbox_dh_set)

    def __init__(self):
        this = _image.new_dbox()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _image.delete_dbox
    __del__ = lambda self: None
dbox_swigregister = _image.dbox_swigregister
dbox_swigregister(dbox)


def float_to_box(f):
    return _image.float_to_box(f)
float_to_box = _image.float_to_box

def box_iou(a, b):
    return _image.box_iou(a, b)
box_iou = _image.box_iou

def box_rmse(a, b):
    return _image.box_rmse(a, b)
box_rmse = _image.box_rmse

def diou(a, b):
    return _image.diou(a, b)
diou = _image.diou

def do_nms(boxes, probs, total, classes, thresh):
    return _image.do_nms(boxes, probs, total, classes, thresh)
do_nms = _image.do_nms

def do_nms_sort(boxes, probs, total, classes, thresh):
    return _image.do_nms_sort(boxes, probs, total, classes, thresh)
do_nms_sort = _image.do_nms_sort

def do_nms_obj(boxes, probs, total, classes, thresh):
    return _image.do_nms_obj(boxes, probs, total, classes, thresh)
do_nms_obj = _image.do_nms_obj

def decode_box(b, anchor):
    return _image.decode_box(b, anchor)
decode_box = _image.decode_box

def encode_box(b, anchor):
    return _image.encode_box(b, anchor)
encode_box = _image.encode_box

def read_map(filename):
    return _image.read_map(filename)
read_map = _image.read_map

def shuffle(arr, n, size):
    return _image.shuffle(arr, n, size)
shuffle = _image.shuffle

def sorta_shuffle(arr, n, size, sections):
    return _image.sorta_shuffle(arr, n, size, sections)
sorta_shuffle = _image.sorta_shuffle

def free_ptrs(ptrs, n):
    return _image.free_ptrs(ptrs, n)
free_ptrs = _image.free_ptrs

def basecfg(cfgfile):
    return _image.basecfg(cfgfile)
basecfg = _image.basecfg

def alphanum_to_int(c):
    return _image.alphanum_to_int(c)
alphanum_to_int = _image.alphanum_to_int

def int_to_alphanum(i):
    return _image.int_to_alphanum(i)
int_to_alphanum = _image.int_to_alphanum

def read_int(fd):
    return _image.read_int(fd)
read_int = _image.read_int

def write_int(fd, n):
    return _image.write_int(fd, n)
write_int = _image.write_int

def read_all(fd, buffer, bytes):
    return _image.read_all(fd, buffer, bytes)
read_all = _image.read_all

def write_all(fd, buffer, bytes):
    return _image.write_all(fd, buffer, bytes)
write_all = _image.write_all

def read_all_fail(fd, buffer, bytes):
    return _image.read_all_fail(fd, buffer, bytes)
read_all_fail = _image.read_all_fail

def write_all_fail(fd, buffer, bytes):
    return _image.write_all_fail(fd, buffer, bytes)
write_all_fail = _image.write_all_fail

def find_replace(str, orig, rep, output):
    return _image.find_replace(str, orig, rep, output)
find_replace = _image.find_replace

def error(s):
    return _image.error(s)
error = _image.error

def malloc_error():
    return _image.malloc_error()
malloc_error = _image.malloc_error

def file_error(s):
    return _image.file_error(s)
file_error = _image.file_error

def strip(s):
    return _image.strip(s)
strip = _image.strip

def strip_char(s, bad):
    return _image.strip_char(s, bad)
strip_char = _image.strip_char

def top_k(a, n, k, index):
    return _image.top_k(a, n, k, index)
top_k = _image.top_k

def split_str(s, delim):
    return _image.split_str(s, delim)
split_str = _image.split_str

def fgetl(fp):
    return _image.fgetl(fp)
fgetl = _image.fgetl

def parse_csv_line(line):
    return _image.parse_csv_line(line)
parse_csv_line = _image.parse_csv_line

def copy_string(s):
    return _image.copy_string(s)
copy_string = _image.copy_string

def count_fields(line):
    return _image.count_fields(line)
count_fields = _image.count_fields

def parse_fields(line, n):
    return _image.parse_fields(line, n)
parse_fields = _image.parse_fields

def normalize_array(a, n):
    return _image.normalize_array(a, n)
normalize_array = _image.normalize_array

def scale_array(a, n, s):
    return _image.scale_array(a, n, s)
scale_array = _image.scale_array

def translate_array(a, n, s):
    return _image.translate_array(a, n, s)
translate_array = _image.translate_array

def max_index(a, n):
    return _image.max_index(a, n)
max_index = _image.max_index

def constrain(min, max, a):
    return _image.constrain(min, max, a)
constrain = _image.constrain

def constrain_int(a, min, max):
    return _image.constrain_int(a, min, max)
constrain_int = _image.constrain_int

def mse_array(a, n):
    return _image.mse_array(a, n)
mse_array = _image.mse_array

def rand_normal():
    return _image.rand_normal()
rand_normal = _image.rand_normal

def rand_size_t():
    return _image.rand_size_t()
rand_size_t = _image.rand_size_t

def rand_uniform(min, max):
    return _image.rand_uniform(min, max)
rand_uniform = _image.rand_uniform

def rand_scale(s):
    return _image.rand_scale(s)
rand_scale = _image.rand_scale

def rand_int(min, max):
    return _image.rand_int(min, max)
rand_int = _image.rand_int

def sum_array(a, n):
    return _image.sum_array(a, n)
sum_array = _image.sum_array

def mean_array(a, n):
    return _image.mean_array(a, n)
mean_array = _image.mean_array

def mean_arrays(a, n, els, avg):
    return _image.mean_arrays(a, n, els, avg)
mean_arrays = _image.mean_arrays

def variance_array(a, n):
    return _image.variance_array(a, n)
variance_array = _image.variance_array

def mag_array(a, n):
    return _image.mag_array(a, n)
mag_array = _image.mag_array

def dist_array(a, b, n, sub):
    return _image.dist_array(a, b, n, sub)
dist_array = _image.dist_array

def one_hot_encode(a, n, k):
    return _image.one_hot_encode(a, n, k)
one_hot_encode = _image.one_hot_encode

def sec(clocks):
    return _image.sec(clocks)
sec = _image.sec

def find_int_arg(argc, argv, arg, arg4):
    return _image.find_int_arg(argc, argv, arg, arg4)
find_int_arg = _image.find_int_arg

def find_float_arg(argc, argv, arg, arg4):
    return _image.find_float_arg(argc, argv, arg, arg4)
find_float_arg = _image.find_float_arg

def find_arg(argc, argv, arg):
    return _image.find_arg(argc, argv, arg)
find_arg = _image.find_arg

def find_char_arg(argc, argv, arg, arg4):
    return _image.find_char_arg(argc, argv, arg, arg4)
find_char_arg = _image.find_char_arg

def sample_array(a, n):
    return _image.sample_array(a, n)
sample_array = _image.sample_array

def print_statistics(a, n):
    return _image.print_statistics(a, n)
print_statistics = _image.print_statistics
class node(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, node, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, node, name)
    __repr__ = _swig_repr
    __swig_setmethods__["val"] = _image.node_val_set
    __swig_getmethods__["val"] = _image.node_val_get
    if _newclass:
        val = _swig_property(_image.node_val_get, _image.node_val_set)
    __swig_setmethods__["next"] = _image.node_next_set
    __swig_getmethods__["next"] = _image.node_next_get
    if _newclass:
        next = _swig_property(_image.node_next_get, _image.node_next_set)
    __swig_setmethods__["prev"] = _image.node_prev_set
    __swig_getmethods__["prev"] = _image.node_prev_get
    if _newclass:
        prev = _swig_property(_image.node_prev_get, _image.node_prev_set)

    def __init__(self):
        this = _image.new_node()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _image.delete_node
    __del__ = lambda self: None
node_swigregister = _image.node_swigregister
node_swigregister(node)

class list(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, list, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, list, name)
    __repr__ = _swig_repr
    __swig_setmethods__["size"] = _image.list_size_set
    __swig_getmethods__["size"] = _image.list_size_get
    if _newclass:
        size = _swig_property(_image.list_size_get, _image.list_size_set)
    __swig_setmethods__["front"] = _image.list_front_set
    __swig_getmethods__["front"] = _image.list_front_get
    if _newclass:
        front = _swig_property(_image.list_front_get, _image.list_front_set)
    __swig_setmethods__["back"] = _image.list_back_set
    __swig_getmethods__["back"] = _image.list_back_get
    if _newclass:
        back = _swig_property(_image.list_back_get, _image.list_back_set)

    def __init__(self):
        this = _image.new_list()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _image.delete_list
    __del__ = lambda self: None
list_swigregister = _image.list_swigregister
list_swigregister(list)


def make_list():
    return _image.make_list()
make_list = _image.make_list

def list_insert(arg1, arg2):
    return _image.list_insert(arg1, arg2)
list_insert = _image.list_insert

def list_to_array(l):
    return _image.list_to_array(l)
list_to_array = _image.list_to_array

def free_list(l):
    return _image.free_list(l)
free_list = _image.free_list

def free_list_contents(l):
    return _image.free_list_contents(l)
free_list_contents = _image.free_list_contents

def smooth_l1_cpu(n, pred, truth, delta, error):
    return _image.smooth_l1_cpu(n, pred, truth, delta, error)
smooth_l1_cpu = _image.smooth_l1_cpu

def l2_cpu(n, pred, truth, delta, error):
    return _image.l2_cpu(n, pred, truth, delta, error)
l2_cpu = _image.l2_cpu

def softmax(input, n, temp, output):
    return _image.softmax(input, n, temp, output)
softmax = _image.softmax

def dot_cpu(N, X, INCX, Y, INCY):
    return _image.dot_cpu(N, X, INCX, Y, INCY)
dot_cpu = _image.dot_cpu

def copy_cpu(N, X, INCX, Y, INCY):
    return _image.copy_cpu(N, X, INCX, Y, INCY)
copy_cpu = _image.copy_cpu

def fill_cpu(N, ALPHA, X, INCX):
    return _image.fill_cpu(N, ALPHA, X, INCX)
fill_cpu = _image.fill_cpu

def scal_cpu(N, ALPHA, X, INCX):
    return _image.scal_cpu(N, ALPHA, X, INCX)
scal_cpu = _image.scal_cpu

def const_cpu(N, ALPHA, X, INCX):
    return _image.const_cpu(N, ALPHA, X, INCX)
const_cpu = _image.const_cpu

def pow_cpu(N, ALPHA, X, INCX, Y, INCY):
    return _image.pow_cpu(N, ALPHA, X, INCX, Y, INCY)
pow_cpu = _image.pow_cpu

def mul_cpu(N, X, INCX, Y, INCY):
    return _image.mul_cpu(N, X, INCX, Y, INCY)
mul_cpu = _image.mul_cpu

def axpy_cpu(N, ALPHA, X, INCX, Y, INCY):
    return _image.axpy_cpu(N, ALPHA, X, INCX, Y, INCY)
axpy_cpu = _image.axpy_cpu

def mean_cpu(x, batch, filters, spatial, mean):
    return _image.mean_cpu(x, batch, filters, spatial, mean)
mean_cpu = _image.mean_cpu

def variance_cpu(x, mean, batch, filters, spatial, variance):
    return _image.variance_cpu(x, mean, batch, filters, spatial, variance)
variance_cpu = _image.variance_cpu

def normalize_cpu(x, mean, variance, batch, filters, spatial):
    return _image.normalize_cpu(x, mean, variance, batch, filters, spatial)
normalize_cpu = _image.normalize_cpu

def flatten(x, size, layers, batch, forward):
    return _image.flatten(x, size, layers, batch, forward)
flatten = _image.flatten

def reorg_cpu(x, w, h, c, batch, stride, forward, out):
    return _image.reorg_cpu(x, w, h, c, batch, stride, forward, out)
reorg_cpu = _image.reorg_cpu

def shortcut_cpu(batch, w1, h1, c1, add, w2, h2, c2, out):
    return _image.shortcut_cpu(batch, w1, h1, c1, add, w2, h2, c2, out)
shortcut_cpu = _image.shortcut_cpu
# This file is compatible with both classic and new-style classes.


