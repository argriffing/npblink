"""
Model specification code.

"""
from __future__ import division, print_function, absolute_import

import numpy as np
import networkx as nx

from npmctree.util import normalized

__all__ = [
        'get_Q_primary', 'get_primary_to_tol',
        'get_T_and_root', 'get_edge_to_blen',
        'get_rate_on', 'get_rate_off',
        'get_blink_distn', 'get_primary_distn',
        ]


def get_rate_on():
    return 1.0


def get_rate_off():
    return 1.0


def get_primary_distn():
    nprimary = 6
    return normalized(np.ones(nprimary))


def get_blink_distn():
    return normalized(np.array([get_rate_off(), get_rate_on()]))


def get_Q_primary():
    """
    This is like a symmetric codon rate matrix that is not normalized.

    """
    Q_primary = np.array([
        [0, 1, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1, 0],
        ], dtype=float)
    return Q_primary


def get_primary_to_tol():
    """
    Return a map from primary state to tolerance track name.

    This is like a genetic code mapping codons to amino acids.

    """
    return np.array([0, 0, 1, 1, 2, 2], dtype=int)


def get_T_and_root():
    # rooted tree, deliberately without branch lengths
    T = nx.DiGraph()
    T.add_edges_from([
        ('N1', 'N0'),
        ('N1', 'N2'),
        ('N1', 'N5'),
        ('N2', 'N3'),
        ('N2', 'N4'),
        ])
    return T, 'N1'


def get_edge_to_blen():
    edge_to_blen = {
            ('N1', 'N0') : 0.5,
            ('N1', 'N2') : 0.5,
            ('N1', 'N5') : 0.5,
            ('N2', 'N3') : 0.5,
            ('N2', 'N4') : 0.5,
            }
    return edge_to_blen


