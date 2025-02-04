import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

v1 = [0,0.005,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.055,0.06,0.065,0.07,0.075,0.08,0.085,0.09,0.095,0.1,0.105,0.11,0.115,0.12,0.125,0.13,0.135,0.14,0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3,0.305,0.31,0.315,0.32,0.325,0.33,0.335,0.34,0.345,0.35,0.355,0.36,0.365,0.37,0.375,0.38,0.385,0.39,0.395,0.4,0.405,0.41,0.415,0.42,0.425,0.43,0.435,0.44,0.445,0.45,0.455,0.46,0.465,0.47,0.475,0.48,0.485,0.49,0.495,0.5,0.505,0.51,0.515,0.52,0.525,0.53,0.535,0.54,0.545,0.55,0.555,0.56,0.565,0.57,0.575,0.58,0.585,0.59,0.595,0.6,0.605,0.61,0.615,0.62,0.625,0.63,0.635,0.64,0.645,0.65,0.655,0.66,0.665,0.67,0.675,0.68,0.685,0.69,0.695,0.7,0.705,0.71,0.715,0.72,0.725,0.73,0.735,0.74,0.745,0.75,0.755,0.76,0.765,0.77,0.775,0.78,0.785,0.79,0.795,0.8,0.805,0.81,0.815,0.82,0.825,0.83,0.835,0.84,0.845,0.85,0.855,0.86,0.865,0.87,0.875,0.88,0.885,0.89,0.895,0.9,0.905,0.91,0.915,0.92,0.925,0.93,0.935,0.94,0.945,0.95,0.955,0.96,0.965,0.97,0.975,0.98,0.985,0.99,0.995]
v2 = [0,0.05,0.01,0.015,0.02,0.025,0.03,0.035,0.04,0.045,0.05,0.055,0.06,0.065,0.07,0.075,0.08,0.085,0.09,0.095,0.1,0.105,0.11,0.115,0.12,0.125,0.13,0.135,0.14,0.145,0.15,0.155,0.16,0.165,0.17,0.175,0.18,0.185,0.19,0.195,0.2,0.205,0.21,0.215,0.22,0.225,0.23,0.235,0.24,0.245,0.25,0.255,0.26,0.265,0.27,0.275,0.28,0.285,0.29,0.295,0.3,0.305,0.31,0.315,0.32,0.325,0.33,0.335,0.34,0.345,0.35,0.355,0.36,0.365,0.37,0.375,0.38,0.385,0.39,0.395,0.4,0.405,0.41,0.415,0.42,0.425,0.43,0.435,0.44,0.445,0.45,0.455,0.46,0.465,0.47,0.475,0.48,0.485,0.49,0.495,0.5,0.505,0.51,0.515,0.52,0.525,0.53,0.535,0.54,0.545,0.55,0.555,0.56,0.565,0.57,0.575,0.58,0.585,0.59,0.595,0.6,0.605,0.61,0.615,0.62,0.625,0.63,0.635,0.64,0.645,0.65,0.655,0.66,0.665,0.67,0.675,0.68,0.685,0.69,0.695,0.7,0.705,0.71,0.715,0.72,0.725,0.73,0.735,0.74,0.745,0.75,0.755,0.76,0.765,0.77,0.775,0.78,0.785,0.79,0.795,0.8,0.805,0.81,0.815,0.82,0.825,0.83,0.835,0.84,0.845,0.85,0.855,0.86,0.865,0.87,0.875,0.88,0.885,0.89,0.895,0.9,0.905,0.91,0.915,0.92,0.925,0.93,0.935,0.94,0.945,0.95,0.955,0.96,0.965,0.97,0.975,0.98,0.985,0.99,0.995]
v3 = [0.5,0.01,0.502,0.503,0.504,0.505,0.506,0.507,0.508,0.509,0.51,0.511,0.512,0.513,0.514,0.515,0.516,0.517,0.518,0.519,0.52,0.521,0.522,0.523,0.524,0.525,0.526,0.527,0.528,0.529,0.53,0.531,0.532,0.533,0.534,0.535,0.536,0.537,0.538,0.539,0.54,0.541,0.542,0.543,0.544,0.545,0.546,0.547,0.548,0.549,0.55,0.551,0.552,0.553,0.554,0.555,0.556,0.557,0.558,0.559,0.56,0.561,0.562,0.563,0.564,0.565,0.566,0.567,0.568,0.569,0.57,0.571,0.572,0.573,0.574,0.575,0.576,0.577,0.578,0.579,0.58,0.581,0.582,0.583,0.584,0.585,0.586,0.587,0.588,0.589,0.59,0.591,0.592,0.593,0.594,0.595,0.596,0.597,0.598,0.599,0.6,0.601,0.602,0.603,0.604,0.605,0.606,0.607,0.608,0.609,0.61,0.611,0.612,0.613,0.614,0.615,0.616,0.617,0.618,0.619,0.62,0.621,0.622,0.623,0.624,0.625,0.626,0.627,0.628,0.629,0.63,0.631,0.632,0.633,0.634,0.635,0.636,0.637,0.638,0.639,0.64,0.641,0.642,0.643,0.644,0.645,0.646,0.647,0.648,0.649,0.65,0.651,0.652,0.653,0.654,0.655,0.656,0.657,0.658,0.659,0.66,0.661,0.662,0.663,0.664,0.665,0.666,0.667,0.668,0.669,0.67,0.671,0.672,0.673,0.674,0.675,0.676,0.677,0.678,0.679,0.68,0.681,0.682,0.683,0.684,0.685,0.686,0.687,0.688,0.689,0.69,0.691,0.692,0.693,0.694,0.695,0.696,0.697,0.698,0.699,0.7,0.701,0.702,0.703,0.704,0.705,0.706,0.707,0.708,0.709,0.71,0.711,0.712,0.713,0.714,0.715,0.716,0.717,0.718,0.719,0.72,0.721,0.722,0.723,0.724,0.725,0.726,0.727,0.728,0.729,0.73,0.731,0.732,0.733,0.734,0.735,0.736,0.737,0.738,0.739,0.74,0.741,0.742,0.743,0.744,0.745,0.746,0.747,0.748,0.749]
v4 = [0.45,0.451,0.452,0.453,0.454,0.455,0.456,0.457,0.458,0.459,0.46,0.461,0.462,0.463,0.464,0.465,0.466,0.467,0.468,0.469,0.47,0.471,0.472,0.473,0.474,0.475,0.476,0.477,0.478,0.479,0.48,0.481,0.482,0.483,0.484,0.485,0.486,0.487,0.488,0.489,0.49,0.491,0.492,0.493,0.494,0.495,0.496,0.497,0.498,0.499,0.5,0.501,0.502,0.503,0.504,0.505,0.506,0.507,0.508,0.509,0.51,0.511,0.512,0.513,0.514,0.515,0.516,0.517,0.518,0.519,0.52,0.521,0.522,0.523,0.524,0.525,0.526,0.527,0.528,0.529,0.53,0.531,0.532,0.533,0.534,0.535,0.536,0.537,0.538,0.539,0.54,0.541,0.542,0.543,0.544,0.545,0.546,0.547,0.548,0.549,0.55,0.551,0.552,0.553,0.554,0.555,0.556,0.557,0.558,0.559,0.56,0.561,0.562,0.563,0.564,0.565,0.566,0.567,0.568,0.569,0.57,0.571,0.572,0.573,0.574,0.575,0.576,0.577,0.578,0.579,0.58,0.581,0.582,0.583,0.584,0.585,0.586,0.587,0.588,0.589,0.59,0.591,0.592,0.593,0.594,0.595,0.596,0.597,0.598,0.599,0.6,0.601,0.602,0.603,0.604,0.605,0.606,0.607,0.608,0.609,0.61,0.611,0.612,0.613,0.614,0.615,0.616,0.617,0.618,0.619,0.62,0.621,0.622,0.623,0.624,0.625,0.626,0.627,0.628,0.629,0.63,0.631,0.632,0.633,0.634,0.635,0.636,0.637,0.638,0.639,0.64,0.641,0.642,0.643,0.644,0.645,0.646,0.647,0.648,0.649,0.65,0.651,0.652,0.653,0.654,0.655,0.656,0.657,0.658,0.659,0.66,0.661,0.662,0.663,0.664,0.665,0.666,0.667,0.668,0.669,0.67,0.671,0.672,0.673,0.674,0.675,0.676,0.677,0.678,0.679,0.68,0.681,0.682,0.683,0.684,0.685,0.686,0.687,0.688,0.689,0.69,0.691,0.692,0.693,0.694,0.695,0.696,0.697,0.698,0.699,0.7,0.701,0.702,0.703,0.704,0.705,0.706,0.707,0.708,0.709,0.71,0.711,0.712,0.713,0.714,0.715,0.716,0.717,0.718,0.719,0.72,0.721,0.722,0.723,0.724,0.725,0.726,0.727,0.728,0.729,0.73,0.731,0.732,0.733,0.734,0.735,0.736,0.737,0.738,0.739,0.74,0.741,0.742,0.743,0.744,0.745,0.746,0.747,0.748,0.749]
v5 = [0.45,0.451,0.452,0.453,0.454,0.455,0.456,0.457,0.458,0.459,0.46,0.461,0.462,0.463,0.464,0.465,0.466,0.467,0.468,0.469,0.47,0.471,0.472,0.473,0.474,0.475,0.476,0.477,0.478,0.479,0.48,0.481,0.482,0.483,0.484,0.485,0.486,0.487,0.488,0.489,0.49,0.491,0.492,0.493,0.494,0.495,0.496,0.497,0.498,0.499,0.5,0.501,0.502,0.503,0.504,0.505,0.506,0.507,0.508,0.509,0.51,0.511,0.512,0.513,0.514,0.515,0.516,0.517,0.518,0.519,0.52,0.521,0.522,0.523,0.524,0.525,0.526,0.527,0.528,0.529,0.53,0.531,0.532,0.533,0.534,0.535,0.536,0.537,0.538,0.539,0.54,0.541,0.542,0.543,0.544,0.545,0.546,0.547,0.548,0.549,0.55,0.551,0.552,0.553,0.554,0.555,0.556,0.557,0.558,0.559,0.56,0.561,0.562,0.563,0.564,0.565,0.566,0.567,0.568,0.569,0.57,0.571,0.572,0.573,0.574,0.575,0.576,0.577,0.578,0.579,0.58,0.581,0.582,0.583,0.584,0.585,0.586,0.587,0.588,0.589,0.59,0.591,0.592,0.593,0.594,0.595,0.596,0.597,0.598,0.599,0.6,0.601,0.602,0.603,0.604,0.605,0.606,0.607,0.608,0.609,0.61,0.611,0.612,0.613,0.614,0.615,0.616,0.617,0.618,0.619,0.62,0.621,0.622,0.623,0.624,0.625,0.626,0.627,0.628,0.629,0.63,0.631,0.632,0.633,0.634,0.635,0.636,0.637,0.638,0.639,0.64,0.641,0.642,0.643,0.644,0.645,0.646,0.647,0.648,0.649,0.65,0.651,0.652,0.653,0.654,0.655,0.656,0.657,0.658,0.659,0.66,0.661,0.662,0.663,0.664,0.665,0.666,0.667,0.668,0.669,0.67,0.671,0.672,0.673,0.674,0.675,0.676,0.677,0.678,0.679,0.68,0.681,0.682,0.683,0.684,0.685,0.686,0.687,0.688,0.689,0.69,0.691,0.692,0.693,0.694,0.695,0.696,0.697,0.698,0.699,0.7,0.701,0.702,0.703,0.704,0.705,0.706,0.707,0.708,0.709,0.71,0.711,0.712,0.713,0.714,0.715,0.716,0.717,0.718,0.719,0.72,0.721,0.722,0.723,0.724,0.725,0.726,0.727,0.728,0.729,0.73,0.731,0.732,0.733,0.734,0.735,0.736,0.737,0.738,0.739,0.74,0.741,0.742,0.743,0.744,0.745,0.746,0.747,0.748,0.749]
v6 = [0.45,0.45,0.452,0.453,0.454,0.455,0.456,0.457,0.458,0.459,0.46,0.461,0.462,0.463,0.464,0.465,0.466,0.467,0.468,0.469,0.47,0.471,0.472,0.473,0.474,0.475,0.476,0.477,0.478,0.479,0.48,0.481,0.482,0.483,0.484,0.485,0.486,0.487,0.488,0.489,0.49,0.491,0.492,0.493,0.494,0.495,0.496,0.497,0.498,0.499,0.5,0.501,0.502,0.503,0.504,0.505,0.506,0.507,0.508,0.509,0.51,0.511,0.512,0.513,0.514,0.515,0.516,0.517,0.518,0.519,0.52,0.521,0.522,0.523,0.524,0.525,0.526,0.527,0.528,0.529,0.53,0.531,0.532,0.533,0.534,0.535,0.536,0.537,0.538,0.539,0.54,0.541,0.542,0.543,0.544,0.545,0.546,0.547,0.548,0.549,0.55,0.551,0.552,0.553,0.554,0.555,0.556,0.557,0.558,0.559,0.56,0.561,0.562,0.563,0.564,0.565,0.566,0.567,0.568,0.569,0.57,0.571,0.572,0.573,0.574,0.575,0.576,0.577,0.578,0.579,0.58,0.581,0.582,0.583,0.584,0.585,0.586,0.587,0.588,0.589,0.59,0.591,0.592,0.593,0.594,0.595,0.596,0.597,0.598,0.599,0.6,0.601,0.602,0.603,0.604,0.605,0.606,0.607,0.608,0.609,0.61,0.611,0.612,0.613,0.614,0.615,0.616,0.617,0.618,0.619,0.62,0.621,0.622,0.623,0.624,0.625,0.626,0.627,0.628,0.629,0.63,0.631,0.632,0.633,0.634,0.635,0.636,0.637,0.638,0.639,0.64,0.641,0.642,0.643,0.644,0.645,0.646,0.647,0.648,0.649,0.65,0.651,0.652,0.653,0.654,0.655,0.656,0.657,0.658,0.659,0.66,0.661,0.662,0.663,0.664,0.665,0.666,0.667,0.668,0.669,0.67,0.671,0.672,0.673,0.674,0.675,0.676,0.677,0.678,0.679,0.68,0.681,0.682,0.683,0.684,0.685,0.686,0.687,0.688,0.689,0.69,0.691,0.692,0.693,0.694,0.695,0.696,0.697,0.698,0.699,0.7,0.701,0.702,0.703,0.704,0.705,0.706,0.707,0.708,0.709,0.71,0.711,0.712,0.713,0.714,0.715,0.716,0.717,0.718,0.719,0.72,0.721,0.722,0.723,0.724,0.725,0.726,0.727,0.728,0.729,0.73,0.731,0.732,0.733,0.734,0.735,0.736,0.737,0.738,0.739,0.74,0.741,0.742,0.743,0.744,0.745,0.746,0.747,0.748,0.749]
v7 = [0.45,0.45,0.452,0.453,0.454,0.455,0.456,0.457,0.458,0.459,0.46,0.461,0.462,0.463,0.464,0.465,0.466,0.467,0.468,0.469,0.47,0.471,0.472,0.473,0.474,0.475,0.476,0.477,0.478,0.479,0.48,0.481,0.482,0.483,0.484,0.485,0.486,0.487,0.488,0.489,0.49,0.491,0.492,0.493,0.494,0.495,0.496,0.497,0.498,0.499,0.5,0.501,0.502,0.503,0.504,0.505,0.506,0.507,0.508,0.509,0.51,0.511,0.512,0.513,0.514,0.515,0.516,0.517,0.518,0.519,0.52,0.521,0.522,0.523,0.524,0.525,0.526,0.527,0.528,0.529,0.53,0.531,0.532,0.533,0.534,0.535,0.536,0.537,0.538,0.539,0.54,0.541,0.542,0.543,0.544,0.545,0.546,0.547,0.548,0.549,0.55,0.551,0.552,0.553,0.554,0.555,0.556,0.557,0.558,0.559,0.56,0.561,0.562,0.563,0.564,0.565,0.566,0.567,0.568,0.569,0.57,0.571,0.572,0.573,0.574,0.575,0.576,0.577,0.578,0.579,0.58,0.581,0.582,0.583,0.584,0.585,0.586,0.587,0.588,0.589,0.59,0.591,0.592,0.593,0.594,0.595,0.596,0.597,0.598,0.599,0.6,0.601,0.602,0.603,0.604,0.605,0.606,0.607,0.608,0.609,0.61,0.611,0.612,0.613,0.614,0.615,0.616,0.617,0.618,0.619,0.62,0.621,0.622,0.623,0.624,0.625,0.626,0.627,0.628,0.629,0.63,0.631,0.632,0.633,0.634,0.635,0.636,0.637,0.638,0.639,0.64,0.641,0.642,0.643,0.644,0.645,0.646,0.647,0.648,0.649,0.65,0.651,0.652,0.653,0.654,0.655,0.656,0.657,0.658,0.659,0.66,0.661,0.662,0.663,0.664,0.665,0.666,0.667,0.668,0.669,0.67,0.671,0.672,0.673,0.674,0.675,0.676,0.677,0.678,0.679,0.68,0.681,0.682,0.683,0.684,0.685,0.686,0.687,0.688,0.689,0.69,0.691,0.692,0.693,0.694,0.695,0.696,0.697,0.698,0.699,0.7,0.701,0.702,0.703,0.704,0.705,0.706,0.707,0.708,0.709,0.71,0.711,0.712,0.713,0.714,0.715,0.716,0.717,0.718,0.719,0.72,0.721,0.722,0.723,0.724,0.725,0.726,0.727,0.728,0.729,0.73,0.731,0.732,0.733,0.734,0.735,0.736,0.737,0.738,0.739,0.74,0.741,0.742,0.743,0.744,0.745,0.746,0.747,0.748,0.749]
v8 = [0.45,0.45,0.452,0.453,0.454,0.455,0.456,0.457,0.458,0.459,0.46,0.461,0.462,0.463,0.464,0.465,0.466,0.467,0.468,0.469,0.47,0.471,0.472,0.473,0.474,0.475,0.476,0.477,0.478,0.479,0.48,0.481,0.482,0.483,0.484,0.485,0.486,0.487,0.488,0.489,0.49,0.491,0.492,0.493,0.494,0.495,0.496,0.497,0.498,0.499,0.5,0.501,0.502,0.503,0.504,0.505,0.506,0.507,0.508,0.509,0.51,0.511,0.512,0.513,0.514,0.515,0.516,0.517,0.518,0.519,0.52,0.521,0.522,0.523,0.524,0.525,0.526,0.527,0.528,0.529,0.53,0.531,0.532,0.533,0.534,0.535,0.536,0.537,0.538,0.539,0.54,0.541,0.542,0.543,0.544,0.545,0.546,0.547,0.548,0.549,0.55,0.551,0.552,0.553,0.554,0.555,0.556,0.557,0.558,0.559,0.56,0.561,0.562,0.563,0.564,0.565,0.566,0.567,0.568,0.569,0.57,0.571,0.572,0.573,0.574,0.575,0.576,0.577,0.578,0.579,0.58,0.581,0.582,0.583,0.584,0.585,0.586,0.587,0.588,0.589,0.59,0.591,0.592,0.593,0.594,0.595,0.596,0.597,0.598,0.599,0.6,0.601,0.602,0.603,0.604,0.605,0.606,0.607,0.608,0.609,0.61,0.611,0.612,0.613,0.614,0.615,0.616,0.617,0.618,0.619,0.62,0.621,0.622,0.623,0.624,0.625,0.626,0.627,0.628,0.629,0.63,0.631,0.632,0.633,0.634,0.635,0.636,0.637,0.638,0.639,0.64,0.641,0.642,0.643,0.644,0.645,0.646,0.647,0.648,0.649,0.65,0.651,0.652,0.653,0.654,0.655,0.656,0.657,0.658,0.659,0.66,0.661,0.662,0.663,0.664,0.665,0.666,0.667,0.668,0.669,0.67,0.671,0.672,0.673,0.674,0.675,0.676,0.677,0.678,0.679,0.68,0.681,0.682,0.683,0.684,0.685,0.686,0.687,0.688,0.689,0.69,0.691,0.692,0.693,0.694,0.695,0.696,0.697,0.698,0.699,0.7,0.701,0.702,0.703,0.704,0.705,0.706,0.707,0.708,0.709,0.71,0.711,0.712,0.713,0.714,0.715,0.716,0.717,0.718,0.719,0.72,0.721,0.722,0.723,0.724,0.725,0.726,0.727,0.728,0.729,0.73,0.731,0.732,0.733,0.734,0.735,0.736,0.737,0.738,0.739,0.74,0.741,0.742,0.743,0.744,0.745,0.746,0.747,0.748,0.749]
v9 = [0.45,0.45,0.452,0.453,0.454,0.455,0.456,0.457,0.458,0.459,0.46,0.461,0.462,0.463,0.464,0.465,0.466,0.467,0.468,0.469,0.47,0.471,0.472,0.473,0.474,0.475,0.476,0.477,0.478,0.479,0.48,0.481,0.482,0.483,0.484,0.485,0.486,0.487,0.488,0.489,0.49,0.491,0.492,0.493,0.494,0.495,0.496,0.497,0.498,0.499,0.5,0.501,0.502,0.503,0.504,0.505,0.506,0.507,0.508,0.509,0.51,0.511,0.512,0.513,0.514,0.515,0.516,0.517,0.518,0.519,0.52,0.521,0.522,0.523,0.524,0.525,0.526,0.527,0.528,0.529,0.53,0.531,0.532,0.533,0.534,0.535,0.536,0.537,0.538,0.539,0.54,0.541,0.542,0.543,0.544,0.545,0.546,0.547,0.548,0.549,0.55,0.551,0.552,0.553,0.554,0.555,0.556,0.557,0.558,0.559,0.56,0.561,0.562,0.563,0.564,0.565,0.566,0.567,0.568,0.569,0.57,0.571,0.572,0.573,0.574,0.575,0.576,0.577,0.578,0.579,0.58,0.581,0.582,0.583,0.584,0.585,0.586,0.587,0.588,0.589,0.59,0.591,0.592,0.593,0.594,0.595,0.596,0.597,0.598,0.599,0.6,0.601,0.602,0.603,0.604,0.605,0.606,0.607,0.608,0.609,0.61,0.611,0.612,0.613,0.614,0.615,0.616,0.617,0.618,0.619,0.62,0.621,0.622,0.623,0.624,0.625,0.626,0.627,0.628,0.629,0.63,0.631,0.632,0.633,0.634,0.635,0.636,0.637,0.638,0.639,0.64,0.641,0.642,0.643,0.644,0.645,0.646,0.647,0.648,0.649,0.65,0.651,0.652,0.653,0.654,0.655,0.656,0.657,0.658,0.659,0.66,0.661,0.662,0.663,0.664,0.665,0.666,0.667,0.668,0.669,0.67,0.671,0.672,0.673,0.674,0.675,0.676,0.677,0.678,0.679,0.68,0.681,0.682,0.683,0.684,0.685,0.686,0.687,0.688,0.689,0.69,0.691,0.692,0.693,0.694,0.695,0.696,0.697,0.698,0.699,0.7,0.701,0.702,0.703,0.704,0.705,0.706,0.707,0.708,0.709,0.71,0.711,0.712,0.713,0.714,0.715,0.716,0.717,0.718,0.719,0.72,0.721,0.722,0.723,0.724,0.725,0.726,0.727,0.728,0.729,0.73,0.731,0.732,0.733,0.734,0.735,0.736,0.737,0.738,0.739,0.74,0.741,0.742,0.743,0.744,0.745,0.746,0.747,0.748,0.749]

def getVList(n):
    match n:
        case 1:
            return (v1,23.3)
        case 2:
            return (v2,24.5)
        case 3:
            return (v3,24.7)
        case 4:
            return (v4,25.0)
        case 5:
            return (v5,26.1)
        case 6:
            return (v6,26.5)
        case 7:
            return (v7,28.5)
        case 8:
            return (v8,29.0)
        case 9:
            return (v9,29.3)
A1 = [448.203,421.22,403.132,446.887,377.799,383.392,381.418,356.086,370.891,381.089,377.799,386.024,442.281,399.513,424.187,394.578,380.431,422.871,398.855,420.239,395.894,349.835,397.21,394.907,374.839,404.777,405.763,431.754,412.343,424.187,413.659,434.714,397.539,428.135,478.799,445.9,459.389,443.926,412.014,447.874,438.333,476.496,449.848,454.454,428.135,409.382,412.672,408.395,384.05,394.907,412.672,427.806,423.2,449.19,441.294,440.965,414.646,429.451,460.376,430.109,469.916,478.47,482.418,474.851,477.812,542.294,557.098,628.489,672.244,672.244,770.282,865.031,933.132,1064.4,1204.88,1316.4,1549.66,1806.27,2127.03,2480.36,2876.47,3458.45,4196.04,5024.43,5991,7288.53,8791.35,10713,13036.9,15706.7,18902.8,22923,28065.5,33899.4,41104.6,49664.8,60129,73794.5,89311.6,108199,131053,158832,194514,235395,285166,345388,417868,511311,618677,747462,902907,1.09E+06,1.33E+06,1.60E+06,1.93E+06,2.31E+06,2.78E+06,3.32E+06,3.68E+06,3.84E+06,3.98E+06,4.13E+06,4.27E+06,4.43E+06,4.59E+06,4.76E+06,4.94E+06,5.14E+06,5.36E+06,5.59E+06,5.84E+06,6.12E+06,6.42E+06,6.78E+06,7.15E+06,7.56E+06,8.02E+06,8.52E+06,9.11E+06,9.72E+06,1.04E+07,1.12E+07,1.20E+07,1.29E+07,1.39E+07,1.39E+07,1.38E+07,1.38E+07,1.38E+07,1.37E+07,1.37E+07,1.37E+07,1.37E+07,1.37E+07,1.37E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.38E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.40E+07]
A2 = [185682,18566,185619,185703,185661,185682,185703,185640,185682,185682,185661,185703,185682,185661,185682,185682,185703,185703,185682,185703,185640,185661,185682,185703,185682,185703,185661,185703,185640,185703,185682,185703,185703,185661,185703,185703,185682,185703,185703,185682,185703,185703,185703,185682,185682,185682,185682,185661,185703,185661,185682,185682,185703,185661,185703,185703,185682,185661,185703,185703,185703,185703,185682,185703,185703,185682,185661,185703,185682,185682,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,274672,291001,396340,817361,817361,817361,817361,889013,1.03E+06,1.24E+06,1.48E+06,1.87E+06,2.50E+06,2.71E+06,3.13E+06,3.56E+06,4.19E+06,4.19E+06,4.19E+06,4.36E+06,4.40E+06,4.61E+06,4.82E+06,4.92E+06,5.03E+06,5.45E+06,5.87E+06,5.87E+06,6.08E+06,6.29E+06,6.61E+06,7.56E+06,7.56E+06,7.77E+06,8.29E+06,8.82E+06,9.45E+06,1.01E+07,1.08E+07,1.16E+07,1.24E+07,1.33E+07,1.40E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07,1.40E+07]
A3 = [185703,185703,185703,185703,185703,185704,190695,197813,206969,245548,290980,290980,290980,290980,290980,291001,291001,294830,396340,396340,396340,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,853321,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.13E+06,1.13E+06,1.24E+06,1.24E+06,1.24E+06,1.45E+06,1.45E+06,1.45E+06,1.45E+06,1.55E+06,1.66E+06,1.66E+06,1.86E+06,1.87E+06,1.87E+06,1.88E+06,1.98E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.71E+06,2.71E+06,2.71E+06,2.92E+06,2.94E+06,3.13E+06,3.13E+06,3.34E+06,3.55E+06,3.55E+06,3.55E+06,3.66E+06,3.77E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.22E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.50E+06,4.50E+06,4.50E+06,4.61E+06,4.61E+06,4.61E+06,4.75E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.83E+06,4.92E+06,5.01E+06,5.03E+06,5.03E+06,5.03E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.26E+06,5.45E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,6.08E+06,6.08E+06,6.08E+06,6.08E+06,6.15E+06,6.29E+06,6.29E+06,6.29E+06,6.50E+06,6.50E+06,6.50E+06,6.61E+06,6.71E+06,6.71E+06,6.92E+06,6.92E+06,6.92E+06,7.14E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.77E+06,7.77E+06,7.87E+06,7.98E+06,7.98E+06,8.19E+06,8.19E+06,8.40E+06,8.40E+06,8.61E+06,8.81E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.38E+06,9.45E+06,9.66E+06,9.66E+06,9.87E+06,9.99E+06,1.01E+07,1.03E+07,1.09E+07,1.09E+07,1.09E+07,1.09E+07,1.09E+07,1.11E+07,1.13E+07,1.15E+07,1.16E+07,1.18E+07,1.20E+07,1.22E+07,1.26E+07,1.26E+07,1.27E+07,1.30E+07,1.30E+07,1.32E+07,1.35E+07,1.37E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07]
A4 = [185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,186227,194733,201829,234911,290316,290980,290980,290980,290980,291001,291001,291001,395298,396340,396340,695325,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.05E+06,1.13E+06,1.18E+06,1.24E+06,1.24E+06,1.45E+06,1.45E+06,1.45E+06,1.45E+06,1.47E+06,1.66E+06,1.66E+06,1.66E+06,1.87E+06,1.87E+06,1.87E+06,1.98E+06,2.08E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.71E+06,2.71E+06,2.81E+06,2.92E+06,3.13E+06,3.13E+06,3.24E+06,3.34E+06,3.55E+06,3.55E+06,3.57E+06,3.66E+06,3.77E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.41E+06,4.50E+06,4.50E+06,4.61E+06,4.61E+06,4.61E+06,4.61E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.92E+06,4.92E+06,5.03E+06,5.03E+06,5.03E+06,5.06E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.34E+06,5.47E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,6.08E+06,6.08E+06,6.08E+06,6.08E+06,6.19E+06,6.29E+06,6.29E+06,6.50E+06,6.50E+06,6.50E+06,6.51E+06,6.61E+06,6.71E+06,6.72E+06,6.92E+06,6.92E+06,6.92E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.77E+06,7.77E+06,7.97E+06,7.98E+06,8.19E+06,8.19E+06,8.29E+06,8.40E+06,8.47E+06,8.61E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.45E+06,9.54E+06,9.66E+06,9.86E+06,9.87E+06,1.01E+07,1.02E+07,1.03E+07,1.09E+07,1.09E+07,1.09E+07,1.09E+07,1.10E+07,1.11E+07,1.13E+07,1.16E+07,1.17E+07,1.18E+07,1.22E+07,1.26E+07,1.26E+07,1.26E+07,1.28E+07,1.30E+07,1.31E+07,1.33E+07,1.36E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07]
A5 = [185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,187606,194414,205727,262613,290980,290980,290980,290980,291001,291001,301297,396340,396340,704926,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.04E+06,1.13E+06,1.14E+06,1.24E+06,1.24E+06,1.45E+06,1.45E+06,1.45E+06,1.45E+06,1.50E+06,1.57E+06,1.66E+06,1.66E+06,1.87E+06,1.87E+06,1.87E+06,1.96E+06,2.08E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.71E+06,2.71E+06,2.82E+06,2.92E+06,3.13E+06,3.13E+06,3.24E+06,3.34E+06,3.55E+06,3.55E+06,3.58E+06,3.66E+06,3.77E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.50E+06,4.50E+06,4.61E+06,4.61E+06,4.61E+06,4.61E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.92E+06,5.03E+06,5.03E+06,5.03E+06,5.03E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.34E+06,5.35E+06,5.86E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.98E+06,6.08E+06,6.08E+06,6.08E+06,6.19E+06,6.28E+06,6.29E+06,6.29E+06,6.50E+06,6.50E+06,6.50E+06,6.61E+06,6.71E+06,6.71E+06,6.92E+06,6.92E+06,6.92E+06,7.03E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.77E+06,7.77E+06,7.78E+06,7.98E+06,7.98E+06,8.19E+06,8.19E+06,8.29E+06,8.40E+06,8.61E+06,8.61E+06,8.82E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.34E+06,9.45E+06,9.65E+06,9.66E+06,9.87E+06,9.97E+06,1.01E+07,1.03E+07,1.05E+07,1.09E+07,1.09E+07,1.09E+07,1.09E+07,1.11E+07,1.13E+07,1.13E+07,1.16E+07,1.18E+07,1.20E+07,1.25E+07,1.26E+07,1.26E+07,1.26E+07,1.28E+07,1.30E+07,1.32E+07,1.33E+07,1.36E+07,1.39E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07]
A6 = [185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,186371,195114,209063,275946,290980,290980,290980,290980,291001,291001,302960,396340,396340,718738,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.04E+06,1.13E+06,1.13E+06,1.24E+06,1.24E+06,1.45E+06,1.45E+06,1.45E+06,1.45E+06,1.45E+06,1.55E+06,1.66E+06,1.66E+06,1.87E+06,1.87E+06,1.87E+06,1.91E+06,2.04E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.71E+06,2.71E+06,2.71E+06,2.92E+06,3.09E+06,3.13E+06,3.13E+06,3.34E+06,3.55E+06,3.55E+06,3.55E+06,3.66E+06,3.77E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.48E+06,4.50E+06,4.50E+06,4.61E+06,4.61E+06,4.61E+06,4.61E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.92E+06,4.92E+06,5.03E+06,5.03E+06,5.03E+06,5.12E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.34E+06,5.45E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,6.08E+06,6.08E+06,6.08E+06,6.09E+06,6.19E+06,6.29E+06,6.29E+06,6.50E+06,6.50E+06,6.50E+06,6.51E+06,6.61E+06,6.71E+06,6.72E+06,6.92E+06,6.92E+06,7.00E+06,7.41E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.76E+06,7.77E+06,7.77E+06,7.98E+06,7.98E+06,8.19E+06,8.19E+06,8.29E+06,8.40E+06,8.61E+06,8.61E+06,8.71E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.45E+06,9.49E+06,9.66E+06,9.77E+06,9.87E+06,1.01E+07,1.02E+07,1.03E+07,1.09E+07,1.09E+07,1.09E+07,1.09E+07,1.10E+07,1.12E+07,1.13E+07,1.16E+07,1.17E+07,1.19E+07,1.20E+07,1.26E+07,1.26E+07,1.26E+07,1.27E+07,1.30E+07,1.30E+07,1.33E+07,1.35E+07,1.37E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07]
A7 = [185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,186411,193251,279663,290980,290980,290980,291001,291001,369347,396340,396340,626264,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.13E+06,1.13E+06,1.24E+06,1.24E+06,1.36E+06,1.45E+06,1.45E+06,1.45E+06,1.45E+06,1.55E+06,1.66E+06,1.66E+06,1.87E+06,1.87E+06,1.87E+06,1.87E+06,1.99E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.63E+06,2.71E+06,2.71E+06,2.82E+06,2.92E+06,3.13E+06,3.13E+06,3.24E+06,3.35E+06,3.55E+06,3.55E+06,3.66E+06,3.77E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.50E+06,4.50E+06,4.61E+06,4.61E+06,4.61E+06,4.61E+06,4.61E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.92E+06,4.92E+06,5.03E+06,5.03E+06,5.03E+06,5.13E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.34E+06,5.34E+06,5.79E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,6.08E+06,6.08E+06,6.08E+06,6.13E+06,6.28E+06,6.29E+06,6.29E+06,6.50E+06,6.50E+06,6.50E+06,6.52E+06,6.61E+06,6.71E+06,6.72E+06,6.92E+06,6.92E+06,7.03E+06,7.13E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.66E+06,7.77E+06,7.77E+06,7.98E+06,7.98E+06,8.19E+06,8.19E+06,8.29E+06,8.40E+06,8.50E+06,8.61E+06,8.70E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.45E+06,9.45E+06,9.66E+06,9.75E+06,9.87E+06,1.00E+07,1.01E+07,1.03E+07,1.07E+07,1.09E+07,1.09E+07,1.09E+07,1.10E+07,1.11E+07,1.13E+07,1.15E+07,1.16E+07,1.18E+07,1.20E+07,1.26E+07,1.26E+07,1.26E+07,1.27E+07,1.28E+07,1.30E+07,1.32E+07,1.35E+07,1.37E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.41E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.40E+07]
A8 = [18570,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185704,188226,204338,277336,290980,290980,290980,291001,291001,394466,396340,396340,809360,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.04E+06,1.13E+06,1.13E+06,1.24E+06,1.24E+06,1.45E+06,1.45E+06,1.45E+06,1.45E+06,1.45E+06,1.55E+06,1.66E+06,1.66E+06,1.87E+06,1.87E+06,1.87E+06,1.88E+06,2.08E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.71E+06,2.71E+06,2.82E+06,2.92E+06,3.13E+06,3.13E+06,3.27E+06,3.34E+06,3.55E+06,3.55E+06,3.66E+06,3.66E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.50E+06,4.50E+06,4.61E+06,4.61E+06,4.61E+06,4.61E+06,4.61E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.92E+06,4.92E+06,5.03E+06,5.03E+06,5.03E+06,5.06E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.34E+06,5.45E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,6.08E+06,6.08E+06,6.08E+06,6.08E+06,6.19E+06,6.29E+06,6.29E+06,6.37E+06,6.50E+06,6.50E+06,6.50E+06,6.61E+06,6.71E+06,6.71E+06,6.92E+06,6.92E+06,6.92E+06,7.13E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.77E+06,7.77E+06,7.97E+06,7.98E+06,8.11E+06,8.19E+06,8.21E+06,8.40E+06,8.40E+06,8.61E+06,8.61E+06,9.09E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.34E+06,9.45E+06,9.66E+06,9.66E+06,9.87E+06,9.98E+06,1.01E+07,1.03E+07,1.04E+07,1.09E+07,1.09E+07,1.09E+07,1.09E+07,1.11E+07,1.13E+07,1.14E+07,1.16E+07,1.18E+07,1.20E+07,1.22E+07,1.26E+07,1.26E+07,1.26E+07,1.28E+07,1.30E+07,1.31E+07,1.33E+07,1.36E+07,1.39E+07,1.43E+07,1.43E+07,1.43E+07,1.42E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.40E+07]
A9 = [185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,185703,187148,195262,256243,290980,290980,290980,291001,291001,378801,396340,396340,412342,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,817361,915879,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.03E+06,1.13E+06,1.13E+06,1.24E+06,1.24E+06,1.28E+06,1.45E+06,1.45E+06,1.45E+06,1.45E+06,1.55E+06,1.66E+06,1.66E+06,1.80E+06,1.87E+06,1.87E+06,1.87E+06,1.98E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.50E+06,2.71E+06,2.71E+06,2.82E+06,2.92E+06,3.13E+06,3.13E+06,3.24E+06,3.34E+06,3.55E+06,3.55E+06,3.56E+06,3.66E+06,3.77E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.19E+06,4.39E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.40E+06,4.49E+06,4.50E+06,4.51E+06,4.61E+06,4.61E+06,4.61E+06,4.61E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.82E+06,4.92E+06,4.92E+06,5.03E+06,5.03E+06,5.03E+06,5.03E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.24E+06,5.34E+06,5.45E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.87E+06,5.89E+06,6.08E+06,6.08E+06,6.08E+06,6.19E+06,6.29E+06,6.29E+06,6.29E+06,6.50E+06,6.50E+06,6.50E+06,6.61E+06,6.71E+06,6.71E+06,6.92E+06,6.92E+06,6.92E+06,7.03E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.56E+06,7.66E+06,7.77E+06,7.79E+06,7.98E+06,7.98E+06,8.19E+06,8.19E+06,8.29E+06,8.40E+06,8.50E+06,8.61E+06,8.80E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.24E+06,9.45E+06,9.56E+06,9.66E+06,9.77E+06,9.87E+06,1.01E+07,1.02E+07,1.03E+07,1.05E+07,1.09E+07,1.09E+07,1.09E+07,1.10E+07,1.12E+07,1.13E+07,1.16E+07,1.17E+07,1.18E+07,1.20E+07,1.26E+07,1.26E+07,1.26E+07,1.27E+07,1.30E+07,1.30E+07,1.32E+07,1.35E+07,1.37E+07,1.43E+07,1.43E+07,1.43E+07,1.43E+07,1.40E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07,1.39E+07]
def getAList(n):
        match n:
          case 1:
            return A1
          case 2:
            return A2
          case 3:
            return A3
          case 4:
            return A4
          case 5:
            return A5
          case 6:
            return A6
          case 7:
            return A7
          case 8:
            return A8
          case 9:
            return A9

def transCurrent(vBe,vT,iSat):
    return iSat*(np.exp(vBe/vT)-1)

paramList = [tuple()]*9
for i in range(1,10):
    paramList[i-1] = curve_fit(transCurrent,getVList(i)[0],getAList(i))
    print(f"Params are: {paramList[i-1][0]} with err: {np.sqrt(np.diag(paramList[i-1][1]))}")

#params,err = curve_fit(transCurrent,v1,A1)
#print(f"Params are: {params} with err: {np.sqrt(np.diag(err))}")

