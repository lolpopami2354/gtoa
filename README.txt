CLEARSKY TOWER — COMPLETE EXPANDED RADIO & PHONETIC EDITION

COMPLETE GAME. This is not an updater. No older HTML is needed.
Built directly on the supplied day/night and real-screen-outline tower version.

START
Extract the ZIP. Windows: run START-WINDOWS.bat.
macOS: run START-MAC.command or run python3 launch.py in Terminal.
Linux: run python3 launch.py.
Python 3 is required for the optional launcher; no additional Python packages.
The game opens in your browser on a local loopback address. Keep the terminal open; Ctrl+C stops serving.
You may also open index.html directly to play, but the local server is recommended for camera access.

NEW RADIO COMMANDS
Use the full callsign, the aircraft's shown registration, or select an aircraft first.

DAL123 contact ground 121.9
DAL123 contact tower 118.7
DAL123 contact approach 120.7
DAL123 contact center 128.5
DAL123 contact tower               (uses built-in Tower frequency)
DAL123 monitor tower 118.7
DAL123 say altitude
DAL123 say speed
DAL123 say heading
DAL123 say intentions
DAL123 say position
DAL123 say registration
DAL123 say callsign
DAL123 standby
DAL123 continue
DAL123 repeat last transmission
DAL123 say again
DAL123 line up and wait
DAL123 hold short runway 27
DAL123 cancel landing clearance
DAL123 taxi to runway 28 via Alfa Bravo Charlie
DAL123 taxi to gate via Delta Echo Foxtrot
frequency 118.7
change frequency to 121.9

CONTACT VS MONITOR
Contact gives a readback on the previous aircraft frequency, changes the aircraft frequency and schedules a context-specific check-in on the new frequency after two active simulation seconds.
Monitor gives a readback and changes the aircraft frequency but does not schedule a check-in. Monitoring-only aircraft do not send periodic reminder calls until given a contact instruction.
Changing controller frequency and changing an aircraft frequency are separate actions.
Monitor-all is enabled by default. Turn it off to hear only the tuned frequency; off-frequency calls are counted as missed.
A repeated handoff to the same frequency does not award another handoff bonus.
Default game frequencies: Approach 120.700, Tower 118.700, Ground 121.900, Center 128.500. These are fictional game presets.

PILOT REQUESTS
Pilots can request pushback, taxi, crossing, departure, landing, taxi-in and handoff as their state requires.
Unanswered requests can repeat after a delay. A global request cooldown and queue checks limit reminder chatter.
Standby acknowledges and suppresses that aircraft's automatic reminders for 45 active real-time seconds. It does not stop aircraft movement or revoke clearances. Continue clears standby.
Repeat last transmission repeats the selected aircraft's last recorded transmission, not another aircraft's call.
Pilot speech uses consistent browser voices by aircraft ID and spoken airline names/flight digits. Browser voice quality varies.
Emergency calls receive priority in the queued speech, but do not necessarily interrupt an utterance already playing.
These are scripted game responses, not a conversational language model or a complete real-world ATC procedure engine.

LINE UP / HOLD / LANDING CANCELLATION
Line up and wait requires the aircraft to be holding short at its assigned runway, at the front of the departure queue, with the runway available.
It enters and occupies the runway but does not take off, even with assistance enabled. Issue cleared for takeoff when appropriate.
Hold short works for aircraft on or awaiting taxi routes. Explicit holds prevent assisted takeoff or the requested automatic runway crossing. A failed crossing command retains the hold.
Cancelling landing clearance removes landing permission and prevents assistance from immediately restoring it. Give a new landing clearance or instruct go-around. An arrival reaching touchdown without clearance goes around.
Existing commands remain: heading, altitude, speed, approach, landing, takeoff, pushback, taxi, crossing, hold position, resume taxi, go-around and handoff.

PHONETIC ALPHABET / REGISTRATIONS
Each aircraft now has a unique generated registration shown in Settings flight strips and on the radio monitor.
Use that registration as a typed or spelled-out address, for example:
N001BD, say altitude
November zero zero one Bravo Delta, say altitude
Use the actual registration displayed for your aircraft; the example may not exist after a restart.
Airline callsigns continue to work: Delta four eight two resolves to DAL482 when that aircraft exists.
Context matters: Delta in a spoken airline address remains the airline; Delta after via is taxiway D; Delta in a spelled registration is the letter D.

A Alfa          N November
B Bravo         O Oscar
C Charlie       P Papa
D Delta         Q Quebec
E Echo          R Romeo
F Foxtrot       S Sierra
G Golf          T Tango
H Hotel         U Uniform
I India         V Victor
J Juliett       W Whiskey
K Kilo          X X-ray
L Lima          Y Yankee
M Mike          Z Zulu

Accepted aliases include Alpha/Alfa, Juliet/Juliett, Charly/Charley/Charlie, Whisky/Whiskey and X ray/X-ray/Xray.
Open the radio monitor's ALFA-ZULU REFERENCE button to see all 26 words directly on the actual display. Back to Radio Assist restores the callout screen.
The same reference is in Settings. This is a reference on the desk monitor, not a full-screen popup.

TAXIWAYS
Outbound ground routes use Alfa -> Bravo -> Charlie (A -> B -> C).
Inbound gate routes use Delta -> Echo -> Foxtrot (D -> E -> F).
These are fixed simplified route networks, not an arbitrary taxiway graph. Accepted partial route descriptions are completed to the appropriate full route and read back in full; unsupported taxiway letters/orders are rejected.
The clearances move the aircraft along the actual corresponding route. Surface radar and outside markers label A-F.

PRESERVED FEATURES
10-minute full day -> sunset -> night -> sunrise -> day cycle, independent of aircraft movement speed. Pause freezes the cycle.
Settings can hold daytime, sunset, night or sunrise. Auto resumes the current session-clock phase.
1 = yellow outline on real tower windows; 2 = real radar; 3 = real radio assistance; 4 = real flight-operations screen.
Number keys do not open enlarged views, snap the camera or suspend head tracking.
Click a monitor to select it, then interact with its actual perspective-projected buttons or aircraft targets.
Escape clears the outline and closes menus/text entry without moving your head.
Webcam head rotation, lean-to-zoom, recenter, sensitivity, smoothing, dead zones and inversion.
Detailed terminal, aircraft fuselages, wings, engines, windows and gear; layered sky, sun/moon, stars and atmospheric lighting.
Three fictional airport presets, separate real-minute arrivals/departures, starting parking, assisted/manual operations, queues, crossings, pushback, rollout, gate return and turnaround.
Scoring, alerts, emergency arrivals, pause and downloadable JSON session reports. No automatic session save.

CONTROLS / WEBCAM
Drag to look when tracking is off. Wheel adjusts manual zoom. C recenters head/distance calibration and resets zoom.
Hold Space or the talk button, speak, release to transmit. T opens typed entry.
Click Webcam > Enable webcam. Allow access, sit normally and click Set center.
Lean closer to zoom in; return to the calibrated distance for normal zoom. Yellow-outlined monitors remain in the tower view and lean zoom stays live.
Default lean maximum 2x; manual zoom multiplies it, with a 4x combined cap. Large head turns hold the lean target. Face loss holds the previous pose and zoom.
Head rotation and relative face-size zoom only: no eye tracking, measured distance, positional leaning or VR.
Tracking dynamically downloads MediaPipe Tasks Vision 0.10.14 JS/WASM from jsDelivr and a Google Face Landmarker model. Internet is required for those unbundled assets.
The app processes camera frames locally and has no video-upload or recording feature. Stop camera releases tracks and closes the model.
Use localhost/loopback or HTTPS for camera permissions. Speech recognition is separate, browser-dependent and may use an online browser-operated service. Typed commands are always available.

TESTS
JavaScript syntax validation passed.
Headless Chromium checks: full startup; phonetic and typed registration targeting; unknown registration rejection; airline-safe letter parsing; aliases; contact readback and delayed check-in; monitor with no check-in; standby reminder suppression; query/repeat commands; runway line-up without movement; subsequent takeoff; explicit runway hold; rejected-crossing hold preservation; landing cancellation and re-clearance; taxi routes and a single detailed readback; invalid route rejection; physical radio-monitor alphabet toggle.
Recommended runway-first takeoff commands still work.
10-minute lighting repeat, yellow-outline control and synthetic lean zoom remained active. A six-minute simulated session produced landings and departures without JavaScript page errors.
Real camera movement, model inference accuracy, microphone recognition and audible pilot playback still require testing on your device.

LIMITATIONS
Stylized procedural graphics using a software polygon renderer; depth-sorting artifacts are possible. Medium detail may improve performance.
Heavy traffic can exceed capacity and cause congestion or separation alerts. Assistance is not guaranteed conflict-free. Active aircraft limit 70.
All layouts, frequencies, identifiers, flight physics and procedures are game approximations. Not a certified training tool.
ENTERTAINMENT ONLY. NOT FOR NAVIGATION OR REAL OPERATIONAL ATC USE.
