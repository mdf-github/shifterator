"""
relative_shift.py

TODO:
- Check reference and comparison are correct on the KLD shift
- Change the axis / title labels for shifts
"""
import os
import sys
import warnings
import numpy as np
import matplotlib.pyplot as plt

import shifterator.shifterator
from shifterator.helper import *

# ------------------------------------------------------------------------------
# --------------------------- Relative shift classes ---------------------------
# ------------------------------------------------------------------------------
class relative_shift(shifterator.shift):
    def __init__(self, reference, comparison, type2score_ref=None,
                 type2score_comp=None, stop_lens=None, delimiter=','):
        """
        Shift object for calculating the relative shift of a comparison system
        from a reference system

        Parameters
        ----------
        reference, comparison: dict
            keys are types of a system and values are frequencies of those types
        type2score_ref, type2score_comp: dict or str, optional
            if dict, types are keys and values are "scores" associated with each
            type (e.g., sentiment). If str, either the name of a score dict or
            file path to a score dict, where types and scores are given on each
            line, separated by commas. If None and other type2score is None,
            defaults to uniform scores across types. Otherwise defaults to the
            other type2score dict
        stop_lens: iterable of 2-tuples, optional
            denotes intervals that should be excluded when calculating shift
            scores
        """
        shift.__init__(reference, comparison, type2score_ref, type2score_comp,
                       stop_lens=stop_lens, delimiter=delimiter)
        # Rename for interpretability
        self.type2freq_ref = self.type2freq_1
        self.type2freq_comp = self.type2freq_2
        self.type2score_ref = self.type2score_1
        self.type2score_comp = self.type2score_2
        # Clean up old names
        del self.type2freq_1
        del self.type2freq_2
        del self.type2score_1
        del self.type2score_2


class sentiment_shift(relative_shift):
    def __init__(self, reference_text, comparison_text,
                 sent_dict_ref='labMT_english', sent_dict_comp=None,
                 stop_lens=[(4,6)], delimiter=','):
        """
        Shift object for calculating the relative shift of a comparison system
        from a reference system

        Parameters
        ----------
        reference_text, comparison_text: dict
            keys are word types of a text and values are frequencies of those
            types
        type2score_ref, type2score_comp: dict or str, optional
            if dict, word types are keys and values are sentiment scores
            associated with each type. If str, either the name of a sentiment
            dict or file path to a score dict, where types and scores are
            given on each line, separated by commas. If None and other
            type2score is None, defaults to uniform sentment across types, i.e.
            shift is in terms of just frequency, not sentiment.
            Otherwise defaults to the other type2score dict
        stop_lens: iterable of 2-tuples, optional
            denotes intervals that should be excluded when calculating shift
            scores. Defaults to stop lens for labMT sentiment dictionary
        """
        relative_shift.__init__(reference_text, comparison_text,
                                sent_dict_ref, sent_dict_comp, stop_lens,
                                delimiter)

class entropy_shift(relative_shift):
    """

    """
    def __init__(self, reference, comparison, base=2, stop_lens=None):
        # Get surprisal scores
        type2s_ref, type2s_comp = get_surprisal_scores(system_1, system_2,
                                                       base=2, alpha=1)
        # Initialize shift
        relative_shift.__init__(reference, comparison, type2s_ref, type2s_comp,
                                stop_lens)

class kl_divergence_shift(relative_shift):
    """

    """
    def __init__(self, reference, comparison, base=2, stop_lens=None):
        # Get surprisal scores
        type2s_ref, type2s_comp = get_surprisal_scores(system_1, system_2,
                                                       base=2, alpha=1)
        # Initialize shift
        relative_shift.__init__(comparison, comparison, type2surprisal_ref,
                                type2surprisal_comp, stop_lens)
