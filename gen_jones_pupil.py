from poke.poke_core import Rayfront
from poke.poke_math import np
import poke.plotting as plot
import zosapi

pth = "C:/Users/Work/Desktop/iom_modeling/afocal_IOM_half.zmx"
n_film = 1.2 + 1j*7.26

flat_1 = {
    "surf": 3,
    "coating" : n_film,
    "mode": "reflect"
}

oap_1 = {
    "surf": 7,
    "coating": n_film,
    "mode": "reflect"
}

surflist = [flat_1, oap_1]

# rayfront parameters
number_of_rays = 16 # across the entrance pupil
wavelength = 0.6e-6
pupil_radius = 50 # mm
max_field_of_view = 0.08 # degrees

rays = Rayfront(number_of_rays,
                wavelength,
                pupil_radius,
                max_field_of_view,
                circle=False)

rays.as_polarized(surflist)
rays.trace_rayset(pth)
rays.compute_jones_pupil(aloc=np.array([0, 0, 1]))

plot.jones_pupil(rays)

# Generate the polarization polynomial
