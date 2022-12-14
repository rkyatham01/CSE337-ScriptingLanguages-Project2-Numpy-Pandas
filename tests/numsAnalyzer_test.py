import pytest
import sys, os
sys.path.insert(1, os.getcwd())
from src.numsAnalyzer import np, countMissingValues, curve_low_scoring_exams, exams_with_median_gt_K

class TestNumsAnalyzer:
    def test_curve_low_scoring_exams(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        assert (curve_low_scoring_exams(x, 95) == np.array([[100., 7.4, 50.9, 7.4, 87.4], [98.5, 1.5, 100.0, 1.5, 66.8], [82.7, 71.4, 100.0, 0.1, 48.1], [100.0, 87.3, 94.5, 99.0, 78.4]])).all()

    def test_curve_low_scoring_exams_value_error_1(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        with pytest.raises(ValueError):
            curve_low_scoring_exams(x, 101)

    def test_curve_low_scoring_exams_value_error_2(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        with pytest.raises(ValueError):
            curve_low_scoring_exams(x, -1)

    def test_curve_low_scoring_exams_value_error_3(self):
        x = np.array([[100.0,87.3,94.5,99.0,278.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        with pytest.raises(ValueError):
            curve_low_scoring_exams(x, 72)

    def test_curve_low_scoring_exams_value_error_4(self):
        x = np.array([[100.0,87.3,94.5,99.0,278.4],[82.6,-71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,-98.5,np.NaN,65.3]])
        with pytest.raises(ValueError):
            curve_low_scoring_exams(x, 72)

    def test_curve_low_scoring_exams_value_error_5(self):
        x = np.array([[100.0,87.3,94.5,99.0,278.4],[82.6,-71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,-98.5,np.NaN,65.3]])
        with pytest.raises(ValueError):
            curve_low_scoring_exams(x, 72.5)

    def test_exams_with_median_gt_K(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        assert exams_with_median_gt_K(x, 70) == 2

    def test_exams_with_median_gt_K_error_1(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        with pytest.raises(ValueError):
            exams_with_median_gt_K(x, -70)

    def test_exams_with_median_gt_K_error_2(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        with pytest.raises(ValueError):
            exams_with_median_gt_K(x, 170)

    def test_exams_with_median_gt_K_error_3(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[182.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        with pytest.raises(ValueError):
            exams_with_median_gt_K(x, 70)

    def test_exams_with_median_gt_K_error_4(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,-43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        with pytest.raises(ValueError):
            exams_with_median_gt_K(x, 70)

    def test_exams_with_median_gt_K_error_5(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[182.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        with pytest.raises(TypeError):
            exams_with_median_gt_K(x, '70')

    def test_count_missing_values_1(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        assert (countMissingValues(x, 0) == np.array([0, 2, 0, 3, 0])).all()

    def test_count_missing_values_2(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        assert (countMissingValues(x, 1) == np.array([0, 1, 2, 2])).all()

    def test_count_missing_values_3(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        assert (countMissingValues(x, -1) == np.array([0, 1, 2, 2])).all()

    def test_count_missing_values_4(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        assert (countMissingValues(x, -2) == np.array([0, 2, 0, 3, 0])).all()

    def test_count_missing_values_5(self):
        x = np.array([[[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0]], [[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]]])
        assert (countMissingValues(x, 0) == np.array([[0,1,0,1,0],[0,1,0,2,0]])).all()

    def test_count_missing_values_6(self):
        x = np.array([[[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0]], [[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]]])
        assert (countMissingValues(x, -3) == np.array([[0,1,0,1,0],[0,1,0,2,0]])).all()

    def test_count_missing_values_error_1(self):
        x = np.array([[100.0,87.3,94.5,99.0,78.4],[82.6,71.3,99.9,np.NaN,48.0],[92.6,np.NaN,43.5,np.NaN,80.0],[97.0,np.NaN,98.5,np.NaN,65.3]])
        with pytest.raises(ValueError):
            countMissingValues(x, 3.5)

    def test_count_missing_values_error_2(self):
        x = np.array([[[100.0, 87.3, 94.5, 99.0, 78.4],[82.6, 71.3, 99.9, np.NaN, 48.0]], [[92.6, np.NaN, 43.5, np.NaN, 80.0],[97.0, np.NaN, 98.5, np.NaN, 65.3]]])
        with pytest.raises(ValueError):
            countMissingValues(x, -4)
