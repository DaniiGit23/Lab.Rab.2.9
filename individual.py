#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def recursive_min(X, n):
    if n == 1:
        return X[0]
    else:
        return min(X[n-1], recursive_min(X, n-1))


if __name__ == '__main__':
    X = [3.14, 4.71, 0.52, 1.546, 5.544]
    n = len(X)
    print(recursive_min(X, n))
