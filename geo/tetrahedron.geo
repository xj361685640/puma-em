/**********************************************************************
 *
 * tetrahedron.geo
 *
 * Copyright (C) 2016 Idesbald Van den Bosch
 *
 * This file is part of Puma-EM.
 * 
 * Puma-EM is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * Puma-EM is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with Puma-EM.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Suggestions/bugs : <vandenbosch.idesbald@gmail.com>
 *
 **********************************************************************/

lc = 0.0999308193333;

H = 0.06;

Point(1) = {0,H,0,lc};
Point(2) = {0.03,0,-0.01,lc};
Point(3) = {-0.03,0,0.01,lc};
Point(4) = {-0.02,0,-0.04,lc};

Line(1) = {1,2};
Line(2) = {1,3};
Line(3) = {1,4};
Line(4) = {2,3};
Line(5) = {3,4};
Line(6) = {4,2};

Line Loop(1) = {2,-4,-1};
Plane Surface(1) = {1};
Line Loop(2) = {-2,3,-5};
Plane Surface(2) = {2};
Line Loop(3) = {1,-6,-3};
Plane Surface(3) = {3};
Line Loop(4) = {4,5,6};
Plane Surface(4) = {4};

Physical Surface(1)={1,2,3,4}; 
