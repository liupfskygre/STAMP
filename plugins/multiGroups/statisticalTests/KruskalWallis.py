#=======================================================================# Author: Donovan Parks## Perform Kruskal-Wallis H-test for independent groups.## Copyright 2011 Donovan Parks## This file is part of STAMP.## STAMP is free software: you can redistribute it and/or modify# it under the terms of the GNU General Public License as published by# the Free Software Foundation, either version 3 of the License, or# (at your option) any later version.## STAMP is distributed in the hope that it will be useful,# but WITHOUT ANY WARRANTY; without even the implied warranty of# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the# GNU General Public License for more details.## You should have received a copy of the GNU General Public License# along with STAMP.	If not, see <http://www.gnu.org/licenses/>.#======================================================================='''import mathimport sysfrom plugins.multiGroups.AbstractMultiGroupStatsTestPlugin import AbstractMultiGroupStatsTestPluginfrom scipy.stats import kruskalfrom numpy import arrayclass KruskalWallis(AbstractMultiGroupStatsTestPlugin):	'''	Perform Kruskal-Wallis H-test	'''		def __init__(self, preferences):		AbstractMultiGroupStatsTestPlugin.__init__(self, preferences)		self.name = 'Kruskal-Wallis H-test'		def hypothesisTest(self, data):		note = ''		arrayData = []		for group in data:			if len(group) < 5:				note = 'degenerate case: at least one group contains less than 5 samples'				return 1.0, note					arrayData.append(array(group))						try:			H_statistic, pValue = apply(kruskal, arrayData)		except:			pValue = 1.0			note = 'Invalid input data for Kruskal-Wallis H-test.'				return pValue, noteif __name__ == "__main__": 	kw = KruskalWallis()	pValue, note = kw.hypothesisTest([[10, 20, 30], [20, 30, 40], [10, 30, 50, 70]])	print pValue	print note