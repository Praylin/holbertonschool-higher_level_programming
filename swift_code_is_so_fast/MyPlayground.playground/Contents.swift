//: Playground - noun: a place where people can play

import UIKit

enum WeatherType {
    case Sun
    case Cloud
    case Rain
    case Wind
    case Snow
}

func getHaterStatus(weather: WeatherType) -> String? {
    if weather == .Sun {
        return nil
    } else {
        return "Hate"
    }
}

getHaterStatus(.Cloud)