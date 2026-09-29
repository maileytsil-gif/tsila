import Foundation
import CoreGraphics
// usage: cg click x y [n] | cg dbl x y | cg drag x1 y1 x2 y2 | cg move x y | cg scroll x y dy
let a=CommandLine.arguments
func P(_ i:Int)->CGPoint{CGPoint(x:Double(a[i])!,y:Double(a[i+1])!)}
func ev(_ t:CGEventType,_ p:CGPoint,_ c:Int64=1){let e=CGEvent(mouseEventSource:nil,mouseType:t,mouseCursorPosition:p,mouseButton:.left)!;e.setIntegerValueField(.mouseEventClickState,value:c);e.post(tap:.cghidEventTap)}
switch a[1]{
case "move": ev(.mouseMoved,P(2))
case "click": let p=P(2); ev(.mouseMoved,p); usleep(60000); ev(.leftMouseDown,p); usleep(40000); ev(.leftMouseUp,p)
case "dbl": let p=P(2); ev(.mouseMoved,p); usleep(60000); ev(.leftMouseDown,p,1); ev(.leftMouseUp,p,1); usleep(60000); ev(.leftMouseDown,p,2); ev(.leftMouseUp,p,2)
case "drag": let p=P(2),q=P(4); ev(.mouseMoved,p); usleep(60000); ev(.leftMouseDown,p); for i in 1...20 {let t=Double(i)/20; ev(.leftMouseDragged,CGPoint(x:p.x+(q.x-p.x)*t,y:p.y+(q.y-p.y)*t)); usleep(15000)}; ev(.leftMouseUp,q)
case "scroll": let p=P(2); ev(.mouseMoved,p); usleep(50000); let e=CGEvent(scrollWheelEvent2Source:nil,units:.line,wheelCount:1,wheel1:Int32(a[4])!,wheel2:0,wheel3:0)!; e.post(tap:.cghidEventTap)
default: break }
