#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-05-10 09:37:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import math

#### 平衡二叉树
class Node(object):
	"""docstring for Node"""
	def __init__(self):
		super(Node, self).__init__()
		self._value = None
		self._rchild = None
		self._lchild = None
		self._parent = None
		# self._splitPoint = None
	@property
	def value(self):
		return self._value
	@value.setter
	def value(self, value):
		self._value = value
	@property
	def rchild(self):
		return self._rchild
	@rchild.setter
	def rchild(self, rchild):
		self._rchild = rchild
	@property
	def lchild(self):
		return self._lchild
	@lchild.setter
	def lchild(self, lchild):
		self._lchild = lchild
	@property
	def parent(self):
		return parent
	@parent.setter
	def parent(self, parent):
		return parent
	@property
	def splitPoint(self):
		return self._splitPoint

	@splitPoint.setter
	def splitPoint(self, sp):
		self._splitPoint = sp

# def findLastIndex(dataList, index, target):
# 	dataListLen = len(dataList)
# 	start, end = -1, -1
# 	for i in  range(dataListLen):
# 		if dataList[i][index] == target:
# 			if start == -1:
# 				start = i
# 			else:
# 				end = i
# 	end = max(start, end)
# 	return start, end
# def getDistanceList(srcList, target):
# 	resList = list()
# 	for val in srcList:
# 		resList.append(getEucDistance(val, target))
# 	return resList
def getEucDistance(x1,x2):
	sub = [(x1[i] - x2[i]) ** 2 for i in range(len(x1))]
	return math.sqrt(sum(sub))
class kdTree(object):
	"""docstring for kdTree"""
	def __init__(self, k, dataList):
		super(kdTree, self).__init__()
		self.init(k, dataList)

	def init(self, k, dataList, target = None):
		self.k = k
		self.dataList = dataList
		if len(dataList) > 0:
			self.dim = len(dataList[0]) # 单个数据的维度
		self.kbtree = Node()
		self.knears = dict()
		self.knearsList = list()

	def createTree(self, dataList, parent, l):
		if not parent or len(dataList) == 0:
			return
		index = l % self.dim
		parent.splitPoint = index
		sortedDataList = sorted(dataList, key = lambda x: x[index])
		median = len(sortedDataList) // 2
		# median = sortedDataList[len(dataList) // 2][index]
		# startIndex, endIndex = findLastIndex(sortedDataList, index, median)
		leftDataList = sortedDataList[:median]
		rightDataList = sortedDataList[median + 1:]
		parent.value = sortedDataList[median]
		if len(leftDataList):
			parent.lchild = Node()
			parent.lchild.parent = parent
			self.createTree(leftDataList, parent.lchild, l + 1)
		
		if len(rightDataList):
			parent.rchild = Node()
			parent.rchild.parent = parent
			self.createTree(rightDataList, parent.rchild, l + 1)
	# 中序遍历
	def traverse(self, tree):
		if not tree:
			return
		print(tree.value)
		# for val in tree.value:
		# 	print(val)
		self.traverse(tree.lchild)
		self.traverse(tree.rchild)
	def searchK(self, tree, target, l = 0):
		if not tree:
			return False
		index = l % (len(target))
		if tree.value[index] > target[index]:
			self.searchK(tree.lchild, target, l + 1)
		elif tree.value[index] < target[index]:
			self.searchK(tree.rchild, target, l + 1)
		dis = getEucDistance(tree.value, target)
		if len(self.knears) < self.k or dis <= self.knearsList[-1][1]:
			self.knears.setdefault(tree.value, dis)
			self.knearsList = sorted(self.knears.items(), key = lambda x: x[1])
			# pointList = sorted(knears.items(), reverse = True)
		if tree.lchild or tree.rchild:
			gap = tree.value[index] - target[index]
			if abs(gap) < self.knearsList[-1][1]:
				if gap < 0:
					self.searchK(tree.lchild, target, l + 1)
				elif gap > 0:
					self.searchK(tree.rchild, target, l + 1)
	def knn(self, target):
		# self.init(k, dataList, target)
		self.createTree(self.dataList, self.kbtree, 0)
		self.searchK(self.kbtree, target)
		print("success~~")
		return self.knearsList[:self.k]


tree = Node()
dataList = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
# dataList = [(2,3),(2,8),(3,4.5),(5,4),(9,6),(4,7),(4,5.5),(4,6),(4,2),(8,1),(8,7),(8,3),(8,4.5),(7,2),(7,5),(7,8),(7,9)]
kbt = kdTree(2,dataList)
res = kbt.knn((3,4.5))
print(res)

