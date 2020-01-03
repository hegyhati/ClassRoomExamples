#include <gtest/gtest.h>

#include "../src/BrakeDistanceCalc.h"

TEST(VehicleTestSuite, basicBrakeDistance)
{
    szechenyi_programming::Vehicle vehicle({szechenyi_programming::COEFFICIENT_FRICTION, 1200, 10, 1.0});
    ASSERT_NEAR(8.494733, szechenyi_programming::calcBrakeDistance(vehicle), 0.0001);
}

TEST(VehicleTestSuite, basicAverageDistance)
{
    szechenyi_programming::Vehicle vehicle({szechenyi_programming::COEFFICIENT_FRICTION, 1200, 10, 1.0});
    ASSERT_DOUBLE_EQ(150, szechenyi_programming::calcDistance(vehicle, 10));
}

int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}