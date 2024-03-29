import numpy
import pandas


class ReadWriteTestData:
    TEST_DATA = {'Pressure': [50, 60, 70], 'Temperature': [290, 320, 350], 'Flow rate': [0.9, 1.0, 1.1]}
    CSV_PATH = 'Data/params.csv'
    JSON_PATH = 'Data/params.json'


class FunctionsTestData:
    TEST_DATA = {'Pressure': [50, 70], 'Temperature': [290, 350], 'Flow rate': [0.9, 1.0]}
    SUKHAREV_SAMPLE_COUNT = 10
    CENTER_COMPOSITE_CENTER = (1, 1)
    RANDOM_K_MEANS_SAMPLE_COUNT = 8
    HALTON_SAMPLE_COUNT = 10
    UNIFORM_RANDOM_SAMPLE_COUNT = 12
    FULL_FRACT_RESULT = expected = pandas.DataFrame([
        [50, 290, 0.9],
        [70, 290, 0.9],
        [50, 350, 0.9],
        [70, 350, 0.9],
        [50, 290, 1.0],
        [70, 290, 1.0],
        [50, 350, 1.0],
        [70, 350, 1.0]
    ], columns=['Pressure', 'Temperature', 'Flow rate']).astype(float)
    PLACKETT_BURMAN_RESULT = pandas.DataFrame(
        [[50, 290, 1.0],
         [70, 290, 0.9],
         [50, 350, 0.9],
         [70, 350, 1.0]],
        columns=['Pressure', 'Temperature', 'Flow rate']).astype(float)
    SUKHAREV_RESULT = pandas.DataFrame([
        [53.333333, 300, 0.916667],
        [53.333333, 300, 0.95],
        [53.333333, 300, 0.983333],
        [53.333333, 320, 0.916667],
        [53.333333, 320, 0.95],
        [53.333333, 320, 0.983333],
        [53.333333, 340, 0.916667],
        [53.333333, 340, 0.95],
        [53.333333, 340, 0.983333],
        [60, 300, 0.916667],
        [60, 300, 0.95],
        [60, 300, 0.983333],
        [60, 320, 0.916667],
        [60, 320, 0.95],
        [60, 320, 0.983333],
        [60, 340, 0.916667],
        [60, 340, 0.95],
        [60, 340, 0.983333],
        [66.666667, 300, 0.916667],
        [66.666667, 300, 0.95],
        [66.666667, 300, 0.983333],
        [66.666667, 320, 0.916667],
        [66.666667, 320, 0.95],
        [66.666667, 320, 0.983333],
        [66.666667, 340, 0.916667],
        [66.666667, 340, 0.95],
        [66.666667, 340, 0.983333]
    ], columns=['Pressure', 'Temperature', 'Flow rate']).astype(float)
    BOX_BEHNKEN_RESULT = pandas.DataFrame([
        [50, 290, 0.95],
        [70, 290, 0.95],
        [50, 350, 0.95],
        [70, 350, 0.95],
        [50, 320, 0.90],
        [70, 320, 0.90],
        [50, 320, 1.00],
        [70, 320, 1.00],
        [60, 290, 0.90],
        [60, 350, 0.90],
        [60, 290, 1.00],
        [60, 350, 1.00],
        [60, 320, 0.95],
    ], columns=['Pressure', 'Temperature', 'Flow rate']).astype(float)
    CENTRAL_COMPOSITE_RESULT = pandas.DataFrame([
        [50, 290, 0.90],
        [70, 290, 0.90],
        [50, 350, 0.90],
        [70, 350, 0.90],
        [50, 290, 1],
        [70, 290, 1],
        [50, 350, 1],
        [70, 350, 1],
        [60, 320, 0.95],
        [42.361658, 320, 0.95],
        [77.638342, 320, 0.95],
        [60, 267.084974, 0.95],
        [60, 372.915026, 0.95],
        [60, 320, 0.861808],
        [60, 320, 1.038192],
        [60, 320, 0.95],
    ], columns=['Pressure', 'Temperature', 'Flow rate']).astype(float)
    LHS_RESULT = pandas.DataFrame([
        [53.658757, 304.303787, 0.954863],
        [60.299221, 318.473096, 0.920092],
        [66.250581, 347.835460, 0.998789],
    ], columns=['Pressure', 'Temperature', 'Flow rate']).astype(float)
    SPACE_FILLING_LHS_RESULT = pandas.DataFrame([
        [70, 350, 0.90],
        [60, 290, 1.00],
        [50, 320, 0.95],
    ], columns=['Pressure', 'Temperature', 'Flow rate']).astype(float)
    RANDOM_K_MEANS_RESULT = pandas.DataFrame([
        [62.516114, 300.158016, 0.963707],
        [53.742260, 304.255885, 0.943856],
        [54.975888, 334.442503, 0.928774],
        [54.918219, 329.765368, 0.981858],
        [63.935972, 303.433456, 0.921043],
        [66.145022, 312.116375, 0.984434],
        [65.920688, 335.923646, 0.929965],
        [64.166126, 337.323940, 0.977539],
    ], columns=['Pressure', 'Temperature', 'Flow rate']).astype(float)
    MAXIMIN_RESULT = pandas.DataFrame([
        [52.763659, 301.794942, 0.936873],
        [68.389652, 332.854478, 0.999885],
        [62.879804, 315.431303, 0.960639],
    ], columns=['Pressure', 'Temperature', 'Flow rate']).astype(float)
    HALTON_TEST_RESULT = pandas.DataFrame([
        [50, 290, 0.900],
        [60, 310, 0.920],
        [55, 330, 0.940],
        [65, 296.666667, 0.960],
        [52.50, 316.666667, 0.980],
        [62.50, 336.666667, 0.904],
        [57.50, 303.333333, 0.924],
        [67.50, 323.333333, 0.944],
        [51.25, 343.333333, 0.964],
        [61.25, 292.222222, 0.984],
    ], columns=['Pressure', 'Temperature', 'Flow rate']).astype(float)
    UNIFORM_RANDOM_RESULT = pandas.DataFrame([
        [60.976270, 332.911362, 0.960276],
        [60.897664, 315.419288, 0.964589],
        [58.751744, 343.506380, 0.996366],
        [57.668830, 337.503502, 0.952889],
        [61.360891, 345.535798, 0.907104],
        [51.742586, 291.213104, 0.983262],
        [65.563135, 342.200729, 0.997862],
        [65.983171, 317.688762, 0.978053],
        [52.365489, 328.395261, 0.914335],
        [68.893378, 321.310899, 0.941466],
        [55.291112, 336.454021, 0.945615],
        [61.368679, 291.127388, 0.961764],
    ], columns=['Pressure', 'Temperature', 'Flow rate']).astype(float)
