let degrees = 0
let temperature = 0
input.onButtonPressed(Button.A, function () {
    degrees = input.compassHeading()
    if (degrees < 45) {
        basic.showArrow(ArrowNames.North)
    } else if (degrees < 135) {
        basic.showArrow(ArrowNames.East)
    } else if (degrees < 225) {
        basic.showArrow(ArrowNames.South)
    } else if (degrees < 315) {
        basic.showArrow(ArrowNames.West)
    } else {
        basic.showArrow(ArrowNames.North)
    }
})
input.onButtonPressed(Button.AB, function () {
    temperature = input.temperature()
    basic.showNumber(temperature)
    basic.showString("C")
})
input.onButtonPressed(Button.B, function () {
    degrees = input.compassHeading()
    if (degrees < 23) {
        basic.showArrow(ArrowNames.North)
    } else if (degrees < 68) {
        basic.showArrow(ArrowNames.NorthEast)
    } else if (degrees < 113) {
        basic.showArrow(ArrowNames.East)
    } else if (degrees < 158) {
        basic.showArrow(ArrowNames.SouthEast)
    } else if (degrees < 203) {
        basic.showArrow(ArrowNames.South)
    } else if (degrees < 248) {
        basic.showArrow(ArrowNames.SouthWest)
    } else if (degrees < 293) {
        basic.showArrow(ArrowNames.West)
    } else if (degrees < 238) {
        basic.showArrow(ArrowNames.NorthWest)
    } else {
        basic.showArrow(ArrowNames.North)
    }
})
