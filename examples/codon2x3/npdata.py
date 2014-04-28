"""
This module defines some observed data for a toy model.

The point is to check inferences or posterior summaries using this data.
Because the model and data is so small, Monte Carlo summaries can be compared
to analytical summaries that compute the matrix exponential of the compound
continuous time Markov process.

This module has four data levels defining a 'filtration' in the sense
that each level adds information without contradicting or losing
information from any previous level.

"""
from __future__ import division, print_function, absolute_import

import numpy as np


def get_data(level=0):
    """
    Get some data.

    Parameters
    ----------
    level : {0, 1, 2, 3}
        Higher levels add more data, while level zero has no data.

    Returns
    -------
    primary_data : dict
        Map from tree graph node to allowed primary states.
    tol_data : dict
        Map from tolerance class to a map from tree graph node to allowed
        tolerance states.

    """
    if data_level == 0:

        # No restriction on primary process data.
        primary_data = {
                'N0' : np.array([1, 1, 1, 1, 1, 1], dtype=bool),
                'N1' : np.array([1, 1, 1, 1, 1, 1], dtype=bool),
                'N2' : np.array([1, 1, 1, 1, 1, 1], dtype=bool),
                'N3' : np.array([1, 1, 1, 1, 1, 1], dtype=bool),
                'N4' : np.array([1, 1, 1, 1, 1, 1], dtype=bool),
                'N5' : np.array([1, 1, 1, 1, 1, 1], dtype=bool),
                }

        # No restriction on tolerance process data.
        tol_data = {
                0 : {
                    'N0' : np.array([1, 1], dtype=bool),
                    'N1' : np.array([1, 1], dtype=bool),
                    'N2' : np.array([1, 1], dtype=bool),
                    'N3' : np.array([1, 1], dtype=bool),
                    'N4' : np.array([1, 1], dtype=bool),
                    'N5' : np.array([1, 1], dtype=bool),
                    },
                1 : {
                    'N0' : np.array([1, 1], dtype=bool),
                    'N1' : np.array([1, 1], dtype=bool),
                    'N2' : np.array([1, 1], dtype=bool),
                    'N3' : np.array([1, 1], dtype=bool),
                    'N4' : np.array([1, 1], dtype=bool),
                    'N5' : np.array([1, 1], dtype=bool),
                    },
                2 : {
                    'N0' : np.array([1, 1], dtype=bool),
                    'N1' : np.array([1, 1], dtype=bool),
                    'N2' : np.array([1, 1], dtype=bool),
                    'N3' : np.array([1, 1], dtype=bool),
                    'N4' : np.array([1, 1], dtype=bool),
                    'N5' : np.array([1, 1], dtype=bool),
                    },
                }


    elif data_level == 1:

        # Alignment data only.
        # The alignment completely determines the primary state
        # at leaf nodes but does not directly give any information
        # about the state at internal nodes in the tree graph.
        primary_data = {
                'N0' : np.array([1, 0, 0, 0, 0, 0], dtype=bool),
                'N1' : np.array([1, 1, 1, 1, 1, 1], dtype=bool),
                'N2' : np.array([1, 1, 1, 1, 1, 1], dtype=bool),
                'N3' : np.array([0, 0, 0, 0, 1, 0], dtype=bool),
                'N4' : np.array([0, 0, 0, 0, 0, 1], dtype=bool),
                'N5' : np.array([0, 1, 0, 0, 0, 0], dtype=bool),
                }

        # Alignment data only.
        # The alignment partially determines tolerance states at the leaves,
        # in the sense that the observed residue at a leaf cannot be in the
        # untolerated state.
        tol_data = {
                0 : {
                    'N0' : np.array([0, 1], dtype=bool),
                    'N1' : np.array([1, 1], dtype=bool),
                    'N2' : np.array([1, 1], dtype=bool),
                    'N3' : np.array([1, 1], dtype=bool),
                    'N4' : np.array([1, 1], dtype=bool),
                    'N5' : np.array([0, 1], dtype=bool),
                    },
                1 : {
                    'N0' : np.array([1, 1], dtype=bool),
                    'N1' : np.array([1, 1], dtype=bool),
                    'N2' : np.array([1, 1], dtype=bool),
                    'N3' : np.array([1, 1], dtype=bool),
                    'N4' : np.array([1, 1], dtype=bool),
                    'N5' : np.array([1, 1], dtype=bool),
                    },
                2 : {
                    'N0' : np.array([1, 1], dtype=bool),
                    'N1' : np.array([1, 1], dtype=bool),
                    'N2' : np.array([1, 1], dtype=bool),
                    'N3' : np.array([0, 1], dtype=bool),
                    'N4' : np.array([0, 1], dtype=bool),
                    'N5' : np.array([1, 1], dtype=bool),
                    },
                }

    elif data_level == 2:

        # This level adds disease data at tree graph node N0.
        # In particular at N0 tolerance class 0 is in state 1,
        # tolerance class 1 is in state 0,
        # and tolerance class 2 is in state 1.
        primary_data = {
                'N0' : np.array([1, 0, 0, 0, 0, 0], dtype=bool),
                'N1' : np.array([1, 1, 1, 1, 1, 1], dtype=bool),
                'N2' : np.array([1, 1, 1, 1, 1, 1], dtype=bool),
                'N3' : np.array([0, 0, 0, 0, 1, 0], dtype=bool),
                'N4' : np.array([0, 0, 0, 0, 0, 1], dtype=bool),
                'N5' : np.array([0, 1, 0, 0, 0, 0], dtype=bool),
                }
        tol_data = {
                0 : {
                    'N0' : np.array([0, 1], dtype=bool),
                    'N1' : np.array([1, 1], dtype=bool),
                    'N2' : np.array([1, 1], dtype=bool),
                    'N3' : np.array([1, 1], dtype=bool),
                    'N4' : np.array([1, 1], dtype=bool),
                    'N5' : np.array([0, 1], dtype=bool),
                    },
                1 : {
                    'N0' : np.array([1, 0], dtype=bool),
                    'N1' : np.array([1, 1], dtype=bool),
                    'N2' : np.array([1, 1], dtype=bool),
                    'N3' : np.array([1, 1], dtype=bool),
                    'N4' : np.array([1, 1], dtype=bool),
                    'N5' : np.array([1, 1], dtype=bool),
                    },
                2 : {
                    'N0' : np.array([0, 1], dtype=bool),
                    'N1' : np.array([1, 1], dtype=bool),
                    'N2' : np.array([1, 1], dtype=bool),
                    'N3' : np.array([0, 1], dtype=bool),
                    'N4' : np.array([0, 1], dtype=bool),
                    'N5' : np.array([1, 1], dtype=bool),
                    },
                }


    elif data_level == 3:

        # This level adds complete disease data at all leaf nodes.
        primary_data = {
                'N0' : np.array([1, 0, 0, 0, 0, 0], dtype=bool),
                'N1' : np.array([1, 1, 1, 1, 1, 1], dtype=bool),
                'N2' : np.array([1, 1, 1, 1, 1, 1], dtype=bool),
                'N3' : np.array([0, 0, 0, 0, 1, 0], dtype=bool),
                'N4' : np.array([0, 0, 0, 0, 0, 1], dtype=bool),
                'N5' : np.array([0, 1, 0, 0, 0, 0], dtype=bool),
                }
        tol_data = {
                0 : {
                    'N0' : np.array([0, 1], dtype=bool),
                    'N1' : np.array([1, 1], dtype=bool),
                    'N2' : np.array([1, 1], dtype=bool),
                    'N3' : np.array([0, 1], dtype=bool),
                    'N4' : np.array([0, 1], dtype=bool),
                    'N5' : np.array([0, 1], dtype=bool),
                    },
                1 : {
                    'N0' : np.array([1, 0], dtype=bool),
                    'N1' : np.array([1, 1], dtype=bool),
                    'N2' : np.array([1, 1], dtype=bool),
                    'N3' : np.array([0, 1], dtype=bool),
                    'N4' : np.array([0, 1], dtype=bool),
                    'N5' : np.array([0, 1], dtype=bool),
                    },
                2 : {
                    'N0' : np.array([0, 1], dtype=bool),
                    'N1' : np.array([1, 1], dtype=bool),
                    'N2' : np.array([1, 1], dtype=bool),
                    'N3' : np.array([0, 1], dtype=bool),
                    'N4' : np.array([0, 1], dtype=bool),
                    'N5' : np.array([0, 1], dtype=bool),
                    },
                }
    else:
        raise Exception('invalid data level')

    return primary_data, tol_data

