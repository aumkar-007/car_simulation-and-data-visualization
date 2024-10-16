#define _USE_MATH_DEFINES

#include <iostream>
#include <cmath>
#include <chrono>
#include <fstream>
#include <random>

const double EARTH_RADIUS = 6371000;
const double DIM = 111320;   
const double PI = M_PI;

class Car{
    private:
        double latitude;
        double longitude;
        double speed;
        double direction;
        double acceleration;
        double proximity;
        std::mt19937 rng;
    public:
        Car(double lat, double lon, double spe, double dir): latitude(lat), longitude(lon), speed(spe), direction(dir), acceleration(0), proximity(1.0), rng(std::random_device{}())
        {}

        void updateAcceleration(){
            std:: uniform_real_distribution<double> acce_rng(-5.0,5.0);
            acceleration = acce_rng(rng);
            if(speed>60){
                acceleration = -abs(acceleration);
            }
            if(speed<20){
                acceleration = abs(acceleration);
            }
        }

        void updateDirection(){
            std:: uniform_real_distribution<double> dir_rng(-45.0,45.0);
            direction += dir_rng(rng);
            if(direction>360){
                direction -=360;
            }
            if(direction<0){
                direction +=360;
            }
        }

        void updateProximity(double x){
            if(x){
            std:: uniform_real_distribution<double> proxi_rng(0.1,abs(x)+0.1);
            proximity = proxi_rng(rng);}
        }

        inline double degtorad(double d){
            return 2*PI*(d/360.0);
        }

        void move(double time_step){
            double distance;
            updateAcceleration();
            updateProximity(acceleration);
            distance = speed*time_step + 0.5*acceleration*time_step*time_step;
            speed += acceleration*time_step;
            updateDirection();
            double rad = degtorad((direction));
            latitude += (distance*cos(rad))/DIM; 
            longitude += (distance*sin(rad))/DIM; 
        }

        void simulation(const std::string &filename, double time, double time_step){
            std:: ofstream file(filename);
            if(!file.is_open()){
                std::cerr<<"Error while opening file."<<std::endl;
            }
            file << "index,speed,acceleration,direction,latitude,longitude,proximity\n";
            int idx=0;
            while(time){
                move(time_step);
                time -= time_step;
                idx++;
                file<<idx<<","<<speed<<","<<acceleration<<","<<direction<<","<<latitude<<","<<longitude<<","<<proximity<<std::endl;
            }
        }
};

int main(){
    double lat = 12.9638282;
    double lon = 77.7190293;
    double speed = 50.0;
    double dir = 10.0;
    Car Car(lat,lon,speed,dir);
    Car.simulation("car_sim.csv",3600.0,1.0);
    return 0;
}