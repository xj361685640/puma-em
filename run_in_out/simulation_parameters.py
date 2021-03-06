#######################################################################
##
## simulation_parameters.py
##
## Copyright (C) 2016 Idesbald Van den Bosch
##
## This file is part of Puma-EM.
## 
## Puma-EM is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## Puma-EM is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with Puma-EM.  If not, see <http://www.gnu.org/licenses/>.
##
## Suggestions/bugs : <vandenbosch.idesbald@gmail.com>
##
#######################################################################

# we import the base parameters
# if you want to modify them, you can do it here
# or in MLFMA_parameters.py
from MLFMA_parameters import *
from EM_constants import *

# the geometry or target we are going to use in the simulations.
# The list of targets can be viewed by looking up the geo directory
params_simu.pathToTarget = './geo'
params_simu.targetName = 'cubi'
# frequency
params_simu.f = 2.12e9
# the lc (characteristic length) factor -- it will multiply lambda (the wavelength)
# to obtain the average edge length (lc) of the mesh. Usually: lc ~= lambda/10.
params_simu.lc_factor = 1.0/9.5
# the dimensions of the target (if applicable)
params_simu.lx = .2
params_simu.ly = .2
params_simu.lz = .2
# the vertical offset of the target -- shifts the target up or down the z-axis
params_simu.z_offset = 0.0
# the dimensions scaling factor (some targets are designed in other units than meters)
# if dimensions are in cm, params_simu.targetDimensions_scaling_factor = 0.01
# if dimensions are in mm, params_simu.targetDimensions_scaling_factor = 0.001
params_simu.targetDimensions_scaling_factor = 1.0

# CAD and meshing tools
# the following parameter tells if we want to mesh (True) on-the-fly with GMSH.
# If False, it assumes that the mesh file already exists.
# If the mesh comes from another program, like GiD, this parameter will have no impact.
params_simu.meshToMake = True
# the mesh format. Currently only 3 are supported.
MESH_FORMAT = ['GMSH', 'GiD', 'ANSYS']
# GMSH is the default meshing program
params_simu.meshFormat = MESH_FORMAT[0]
# you shouldn't change the following 7 lines
if params_simu.meshFormat in ['GiD', 'ANSYS']:
    params_simu.meshToMake = False
# the termination of the mesh file -- don't change this
if (params_simu.meshFormat == 'GMSH') or (params_simu.meshFormat == 'GiD'):
    params_simu.meshFileTermination = '.msh'
elif (params_simu.meshFormat == 'ANSYS'):
    params_simu.meshFileTermination = '.lis'

#relative epsilon and mu of the host medium
params_simu.eps_r = 1. + 0.j
params_simu.mu_r = 1. + 0.j

# computation settings. Bistatic computation is default.
# one can compute a bistatic excitation, followed by monostatic,
# followed by SAR imaging. Just be aware of the computation time.
params_simu.BISTATIC = 1
params_simu.MONOSTATIC_RCS = 0
params_simu.MONOSTATIC_SAR = 0
# the following is important only if params_simu.MONOSTATIC_RCS == 1
# or if params_simu.MONOSTATIC_SAR == 1
# can only be 1 (True) or 0 (False)
params_simu.COMPUTE_RCS_HH = 1
params_simu.COMPUTE_RCS_VV = 1
params_simu.COMPUTE_RCS_HV = 0
params_simu.COMPUTE_RCS_VH = 0
# safeguard against bad user choices
if (params_simu.COMPUTE_RCS_HH==0) and (params_simu.COMPUTE_RCS_VV==0):
    params_simu.COMPUTE_RCS_VV = 1

# the phase center. It is used for scattered far field computations in the bistatic case, 
# as well as for the phase center for incoming plane wave excitation in the bistatic case.
# It is used as the phase center for antenna problems (also bistatic case).
# In the monostatic case, it is also used for the excitation and the far fields computation. 
# Should be [0.0, 0.0, 0.0], unless you know what you do.
params_simu.r_phase_center = [0.0, 0.0, 0.0]

# Bistatic computation settings
# 1. EXCITATION
###############
# type, strenght and phase and direction, origin of the source.
# It will not be used in case of monostatic_RCS computation
# we have 2 types of excitation: 
# - plurality of dipoles (1 dipole is ok)
# - plane wave
# We can have these excitations separately or at the same time, i.e.,
# plane wave and dipoles.
params_simu.BISTATIC_EXCITATION_DIPOLES = 1
params_simu.BISTATIC_EXCITATION_PLANE_WAVE = 0
# now the details of each excitation
# the name (with path) of the user-supplied excitation file. Set to "" if empty
params_simu.BISTATIC_EXCITATION_J_DIPOLES_FILENAME = "J_dipoles.txt"
params_simu.BISTATIC_EXCITATION_M_DIPOLES_FILENAME = ""
# the structure of the excitation file MUST BE AS FOLLOWS:
# 1 line per dipole, as many lines as there are dipoles
# each line has 9 columns that must be arranged as follows:
#
# real(J_x) imag(J_x) real(J_y) imag(J_y) real(J_z) imag(J_z) r_x r_y r_z
#
# where J = [J_x J_y J_z] is the dipole and r = [r_x r_y r_z] its origin.

if params_simu.BISTATIC_EXCITATION_PLANE_WAVE == 1:
    # origin, strength, phase and polarization of the plane wave
    params_simu.theta_inc = pi/2.0
    params_simu.phi_inc = pi/2.0
    params_simu.E_inc_theta = 1.0+0.j # the theta component
    params_simu.E_inc_phi = 0.0+0.j # the phi component

# 2. OBSERVATION
################
# is it an antenna diagram?
params_simu.ANTENNA_PATTERN = 0
# sampling points: sampling of the resulting field at user-specified points in space.
# It will be used only for BISTATIC
params_simu.BISTATIC_R_OBS = 1
# the name (with path) of the user-supplied r_obs file. Set to "" if empty
params_simu.BISTATIC_R_OBS_FILENAME = "r_obs.txt"
# the structure of the r_obs file MUST BE AS FOLLOWS:
# 1 line per observation point, as many lines as there are points
# each line has 3 columns that must be arranged as follows:
#
# r_obs_x r_obs_y r_obs_z

# we can also have sampling angles from a user-input file
params_simu.BISTATIC_ANGLES_OBS = 0
# the name (with path) of the user-supplied r_obs file. Set to "" if empty
params_simu.BISTATIC_ANGLES_OBS_FILENAME = "bistatic_angles_obs.txt"
# the structure of the bistatic _angles_obs file MUST BE AS FOLLOWS:
# 1 line per observation angle, as many lines as there are angles
# each line has 2 columns which are the angles in degrees (easier for human reading).
# We must have: 0 <= theta <= 180 degrees (0 is the z axis, 180 is -z).
# likewise, 0 <= phi <= 360 degrees. For theta = 90 degrees, phi = 0 is the x axis, 
# 180 is -x, 360 is x.
#
# theta_obs phi_obs


# the angles for the monostatic RCS or the bistatic far-field data.
# Normally the code provides "best angles of observation", best
# from a "field spatial information for minimal sampling size" point of view.
# if you want the program to choose the best points, set AUTOMATIC to True.
# if you want to provide your own sampling points (because you need less/more angles,
# for example), set AUTOMATIC to False. If you chose 1 point only, and AUTOMATIC is False,
# then the point will correspond to START_THETA for thetas and START_PHI for phis.
# thetas
params_simu.START_THETA = pi/2.0
params_simu.STOP_THETA = pi
params_simu.AUTOMATIC_THETAS = False
params_simu.USER_DEFINED_NB_THETA = 1
# phis
params_simu.START_PHI = 0.0
params_simu.STOP_PHI = 2.0 * pi
params_simu.AUTOMATIC_PHIS = True
params_simu.USER_DEFINED_NB_PHI = 200
# monostatic angles can be defined from a file. 
# They will take precedence over the previous definition.
params_simu.ANGLES_FROM_FILE = 0
if params_simu.ANGLES_FROM_FILE == 1:
    # the name (with path) of the user-supplied r_obs file. Set to "" if empty
    params_simu.ANGLES_FILENAME = "monostatic_RCS_angles.txt"
    # the structure of the angles file MUST BE AS FOLLOWS:
    # 1 line per angle, as many lines as there are angles
    # each line has 2 columns  which are the angles in degrees (easier for human reading):
    #
    # theta phi

# for the monostatic SAR settings
if params_simu.MONOSTATIC_SAR==1:
    # dipole antenna will "fly" in a plane defined by local x and y axis
    # we also need an origin for the plane, and a distribution of observation points
    params_simu.SAR_local_x_hat = [-1.0, 0.0, 0.0]
    params_simu.SAR_local_y_hat = [0.0, 0.0, 1.0]
    params_simu.SAR_plane_origin = [0.0, 50.0, 0.0]
    # span of the scanning rectangle (in meters)
    params_simu.SAR_x_span = 200.
    params_simu.SAR_y_span = 200.
    # offset of the scanning rectangle wrt its origin
    params_simu.SAR_x_span_offset = -100.
    params_simu.SAR_y_span_offset = -100.
    # the number of points in each direction
    params_simu.SAR_N_x_points = 8
    params_simu.SAR_N_y_points = 3

# SOLVER DATA
# iterative solver tolerance
params_simu.TOL = 1.e-3
# iterative solver: BICGSTAB, GMRES, RGMRES or FGMRES
SOLVERS = ["BICGSTAB", "GMRES", "RGMRES", "FGMRES"]
params_simu.SOLVER = SOLVERS[0]
params_simu.MAXITER = 300
# RESTART is only for (F)GMRES
params_simu.RESTART = 30
# inner solver characteristics. will be used only if FGMRES is used
params_simu.INNER_SOLVER = SOLVERS[0]
params_simu.INNER_TOL = 0.25
params_simu.INNER_MAXITER = 15
params_simu.INNER_RESTART = 30
# preconditioner type. No choice here
params_simu.PRECOND = "FROB"

# figure that shows the far field or the RCS of the target
params_simu.SHOW_FIGURE = 0

# CURRENTS_VISUALIZATION tells if we want to create a view of the currents in
# GMSH or not. if 1, you can use GMSH to view the currents that have been created.
# open with GMSH the *.pos files that are in the result directory
# only works if BISTATIC == 1
params_simu.CURRENTS_VISUALIZATION = 0
# we can also save the currents at the centroids of the triangles.
# It will be stored in the result directory
params_simu.SAVE_CURRENTS_CENTROIDS = 0

# now a parameter that tells if we want to be silent (little to no output)
params_simu.VERBOSE = 1

# do we have a thin dielectric sheet or impedance boundary condition?
params_simu.TDS_APPROX = 0 # 0 is default here
if params_simu.TDS_APPROX == 1:
    params_simu.nu = 1. # in this case we only use EFIE
    params_simu.SOLVER = "RGMRES" # BiCGSTAB does not work so good for this type of problem
    # refractive index N (from MEDGYESI-MITSCHANG and WANG, "Hybrid Solutions for Large-Impedance
    # Coated Bodies of Revolution", IEEE Trans. Ant. Prop., Vol 34, n. 11, November 1986)
    # see the article for "valid" values of N
    N = (10. - 1.j*0.2)
    # surface impedance Z_s
    params_simu.Z_s = 377.0 * 1.0/N
    # target name and dimensions
    params_simu.lx = 10.0 * c/(2.0 * pi * params_simu.f) # see MEDGYESI-MITSCHANG and WANG 86
else:
    params_simu.Z_s = 0.0 + 0.0j

