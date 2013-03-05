#=======================================================================# Author: Donovan Parks## Perform Tukey-Kramer post-hoc test.## Copyright 2011 Donovan Parks## This file is part of STAMP.## STAMP is free software: you can redistribute it and/or modify# it under the terms of the GNU General Public License as published by# the Free Software Foundation, either version 3 of the License, or# (at your option) any later version.## STAMP is distributed in the hope that it will be useful,# but WITHOUT ANY WARRANTY; without even the implied warranty of# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the# GNU General Public License for more details.## You should have received a copy of the GNU General Public License# along with STAMP.	If not, see <http://www.gnu.org/licenses/>.#=======================================================================import mathfrom plugins.multiGroups.AbstractPostHocTestPlugin import AbstractPostHocTestPluginfrom metagenomics.MathHelper import variance, meanfrom metagenomics.stats.distributions.QTable import QTablefrom scipy.stats import distributionsimport mathclass TukeyKramer(AbstractPostHocTestPlugin):	'''	Perform Tukey-Kramer post-hoc test.	'''		def __init__(self, preferences):		AbstractPostHocTestPlugin.__init__(self, preferences)		self.name = 'Tukey-Kramer'		self.qtable = QTable(preferences)		def run(self, data, coverage, groupNames):		note = ''				# calculate critical value		N = 0		for i in xrange(0, len(data)):			N += len(data[i])					k = len(data)		dfN = k - 1		dfD = N - len(data)				q_cv = self.qtable.cv(1.0-coverage, k, dfD)				cv001 = self.qtable.cv(0.001, k, dfD)		cv01 = self.qtable.cv(0.01, k, dfD)		cv02 = self.qtable.cv(0.02, k, dfD)		cv05 = self.qtable.cv(0.05, k, dfD)		cv1 = self.qtable.cv(0.1, k, dfD)		# calculate mean of each group		groupMean = []		for i in xrange(0, len(data)):			groupMean.append(mean(data[i]))				# calculate within group variance		withinGroupVar = 0.0		for i in xrange(0, len(data)):			withinGroupVar += (len(data[i])-1)*variance(data[i], groupMean[i])		withinGroupVar /= dfD		withinGroupStdDev = math.sqrt(withinGroupVar)				if withinGroupStdDev == 0:			note = 'degenerate case: within group variance is zero; set to 1e-6.'			withinGroupStdDev = 1e-6		# calculate Fs, effect size, and CI for each pair of groups		pValues = []		effectSize = []		lowerCI = []		upperCI = []		labels = []		for i in xrange(0, len(data)):			for j in xrange(i+1, len(data)):				sqrtInvSampleSize = math.sqrt( (1.0/len(data[i]) + 1.0/len(data[j])) / 2.0 )								# effect size				es = groupMean[i] - groupMean[j]				effectSize.append(es)								# p-value				qs = abs(es) / (withinGroupStdDev*sqrtInvSampleSize)								if qs > cv001:					pValue = '< 0.001'				elif qs > cv01:					pValue = '< 0.01'				elif qs > cv02:					pValue = '< 0.02'				elif qs > cv05:					pValue = '< 0.05'				elif qs > cv1:					pValue = '< 0.1'				else:					pValue = '>= 0.1'				pValues.append(pValue)				# confidence interval				confInter = q_cv * withinGroupStdDev * sqrtInvSampleSize				lowerCI.append(es - confInter)				upperCI.append(es + confInter)								labels.append(groupNames[i] + ' : ' + groupNames[j])					return pValues, effectSize, lowerCI, upperCI, labels, noteif __name__ == "__main__": 	pass