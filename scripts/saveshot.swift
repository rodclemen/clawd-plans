import AppKit
import ScreenSaver

// A throwaway: the real screen saver view, fed sample Stranger Clawds sessions, run for a few seconds offscreen and
// drawn to a PNG. Usage: saveshot <out.png> [place key]
let out = CommandLine.arguments[1]
let place = CommandLine.arguments.count > 2 ? CommandLine.arguments[2] : "hawkinsStarcourt"
let app = NSApplication.shared
app.setActivationPolicy(.prohibited)
Universe.shown = .hawkins
let now = Date().timeIntervalSince1970
func s(_ id: Int, _ ai: String, _ project: String, _ mood: String, _ activity: String?, _ prompt: String?,
       _ agents: [SaverFeed.Agent] = [], accent: UInt32) -> SaverFeed.Session {
    SaverFeed.Session(id: "\(id)", cast: id, assistant: ai, project: project, accent: accent, mood: mood, since: now - 95,
                      activity: activity, prompt: prompt, agents: agents)
}
let feed = SaverFeed(at: now, location: place, sessions: [
    s(9100, "claude", "hawkins-lab", "working", "Edit GateMonitor.swift", "close the gate before anything gets through",
      [SaverFeed.Agent(id: "a1", cast: 9102, task: "Check the walkie batteries"),
       SaverFeed.Agent(id: "a2", cast: 9103, task: "Plan the slingshot")], accent: 0xE8564A),
    s(9000, "codex", "creel-house", "waiting", "Allow this command?", "wind the grandfather clock", accent: 0xB04ACC),
    s(9107, "claude", "scoops-ahoy", "thinking", nil, "translate the Russian broadcast", accent: 0x5AC8FF),
    s(9004, "qwen", "community-pool", "working", "Bash: swift test", "lifeguard the test suite", accent: 0xF0C24A),
    s(9115, "gemini", "hopper-cabin", "idle", nil, "make the morning coffee", accent: 0x8AD06A),
], events: [
    SaverFeed.Event(at: now - 60, text: "Eleven started hawkins-lab"),
    SaverFeed.Event(at: now - 40, text: "Dustin Henderson joined Eleven: Check the walkie batteries"),
    SaverFeed.Event(at: now - 20, text: "Vecna needs you on creel-house"),
], universe: 9)
let view = ClawdClashSaverView(frame: NSRect(x: 0, y: 0, width: 1920, height: 1080), isPreview: false)!
view.feedSource = { feed }
let win = NSWindow(contentRect: view.frame, styleMask: [.borderless], backing: .buffered, defer: false)
win.contentView = view
let end = Date().addingTimeInterval(Double(ProcessInfo.processInfo.environment["SECS"] ?? "") ?? 6)
while Date() < end {
    view.animateOneFrame()
    RunLoop.current.run(until: Date().addingTimeInterval(1.0 / 15))
}
view.animateOneFrame()
let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: 1920, pixelsHigh: 1080, bitsPerSample: 8, samplesPerPixel: 4,
                           hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
let gc = NSGraphicsContext(bitmapImageRep: rep)!
func deepest(_ v: NSView) -> CALayer? { v.layer?.sublayers?.isEmpty == false ? v.layer : v.subviews.lazy.compactMap(deepest).first }
if let layer = deepest(view) { layer.render(in: gc.cgContext) } else { print("no layer") }
try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: out))
print("wrote \(out)")
