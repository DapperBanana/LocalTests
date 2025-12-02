using System;
using System.Threading;

class TrafficSimulation
{
    static char[] road = { ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' };
    static int carPosition = 0;
    static bool directionRight = true;
    static int simulationSpeed = 200; // milliseconds

    static void Main()
    {
        Console.WriteLine("Basic Text-Based Traffic Simulation");
        Console.WriteLine("Press any key to stop the simulation...\n");
        Thread simulationThread = new Thread(RunSimulation);
        simulationThread.Start();

        Console.ReadKey();
        simulationThread.Abort();
    }

    static void RunSimulation()
    {
        while (true)
        {
            Console.Clear();

            // Move car
            if (directionRight)
            {
                carPosition++;
                if (carPosition >= road.Length - 1)
                {
                    directionRight = false;
                }
            }
            else
            {
                carPosition--;
                if (carPosition <= 0)
                {
                    directionRight = true;
                }
            }

            // Generate road with car
            for (int i = 0; i < road.Length; i++)
            {
                road[i] = ' ';
            }
            road[carPosition] = '🚗';

            // Display road
            Console.WriteLine(new string(road));

            Thread.Sleep(simulationSpeed);
        }
    }
}