# https://www.acmicpc.net/problem/1991
# 1991. tree traversal

import sys

class Node:
  def __init__(self, value, right, left):
    self.value = value
    self.right = right
    self.left = left

def preorder(node):
  print(node.value, end = '')
  if node.left != '.' : preorder(tree[node.left])
  if node.right != '.' : preorder(tree[node.right])

def inorder(node):
  if node.left != '.': inorder(tree[node.left])
  print(node.value, end = '')
  if node.right != '.': inorder(tree[node.right])

def postorder(node):
  if node.left != '.' : postorder(tree[node.left])
  if node.right != '.' : postorder(tree[node.right])
  print(node.value, end = '')

N = int(input())
tree = {}
root = []

for line in range(N):
    T = sys.stdin.readline().replace('\n', '').split(' ')
    tree[T[0]] = Node(value = T[0], left = T[1],right = T[2])
    root.append(T[0])

preorder(tree[root[0]])
print()
inorder(tree[root[0]])
print()
postorder(tree[root[0]])