#include "../src/triangle.h"

#include "gtest/gtest.h"

TEST(TriangleTestSuite, triangleEquationCorrect1)
{
    Triangle triangle({3,4,5});
    ASSERT_TRUE(validTriangle(triangle));
}

TEST(TriangleTestSuite, triangleEquationCorrect2)
{
    Triangle triangle({13,12,17});
    ASSERT_TRUE(validTriangle(triangle));
}

TEST(TriangleTestSuite, triangleEquationIncorrect1)
{
    Triangle triangle({13,12,34});
    ASSERT_FALSE(validTriangle(triangle));
}

TEST(TriangleTestSuite, triangleArea)
{
    Triangle triangle({3,4,5});
    ASSERT_DOUBLE_EQ(6.0, calcTriangleArea(triangle));
}

int main(int argc, char** argv)
{
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}