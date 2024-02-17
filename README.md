# JEMADAR-AI: An edge architecture for scheduling devices on smart grid energy consumption

JEMADAR-AI is a cloud-edge-based architecture incorporating a Deep Q-Learning algorithm for optimizing energy consumption in smart homes. By leveraging energy production and consumption forecasts, the algorithm intelligently schedules device operation to non-peak energy consumption periods. To perform the experiments and validate the JAMADAR-AI proposal, several tools were used, such as:
- Fogia;
- Gridlab-D Automation;
- Omnet++ and INET Framework;

In the next lines, more details will be given about each of these parts and their respective source or binary codes for installation or configuration.

## Fogia

Fogia is the deep learning-based neural network responsible for making decisions about equipment scheduling in the architecture. Fogia's source code is available in this project in the fogia subdirectory.

## Gridlab-D Automation

Gridlab-D Automation is a script that automates the process of defining houses and their electrical equipment, scheduling equipment and creating a workload for the [Gridlab-D](https://www.gridlabd.org/) summation software. This script automates part of the simulation process, facilitating the definition of the microgrid's characteristics and the calculation of electrical energy consumption.

## Omnet++

To simulate the network and other necessary components, the [INET Framework](https://inet.omnetpp.org/) was used with [Omnet++](https://omnetpp.org/) in respective versions [2.5](https://inet.omnetpp.org/2014-10-30-INET-2.5.0-released.html) and [4.5](https://github.com/omnetpp/omnetpp/blob/master/WHATSNEW.md#omnet-45-june-2014).



