#include <iostream>
#include <random>

constexpr int CHAIN_LENGTH = 100;

struct TemperatureChain
{
    double temp;
    double humidity;
    TemperatureChain* next;
};

bool temperatureComfortable(const TemperatureChain& temp)
{
    if (temp.temp < 15)
    {
        return false;
    }
    else if (temp.temp > 28)
    {
        return false;
    }   
    return true;
}

void initTemperatureElement(TemperatureChain& temperature)
{
    // Random number generation
    static std::random_device rd;
    static std::mt19937 gen(rd());
    static std::uniform_real_distribution<double> dis_temp(10, 34);
    static std::uniform_real_distribution<double> dis_humidity(0.0, 1.0);
    temperature.temp = dis_temp(gen);
    temperature.humidity = dis_humidity(gen);
}

int main(int argc, char** argv)
{
    TemperatureChain chain[CHAIN_LENGTH];
    // Construct temperature chain
    for (int i = 0; i < CHAIN_LENGTH - 1; i++)
    {
        initTemperatureElement(chain[i]);
        chain[i].next = &chain[i+1];
    }
    initTemperatureElement(chain[CHAIN_LENGTH - 1]);
    chain[CHAIN_LENGTH - 1].next = NULL;
    // Check temperature chain
    TemperatureChain* current_chain = &chain[0];
    while (current_chain->next != NULL)
    {
        std::cout << "Temperature: " << current_chain->temp << "\t" << current_chain->humidity << '\n';
        if (!temperatureComfortable(*current_chain))
        {
            std::cerr << "Uncomfortable temperature reached" << '\n';
            break;
        }
        current_chain = current_chain->next;
    }
    return 0;
}