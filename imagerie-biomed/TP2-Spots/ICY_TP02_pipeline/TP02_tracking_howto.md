# How to run inside ICY

## A. With the **Script Editor (Groovy)**
1) Open ICY.
2) Plugins → Scripting → Script Editor → choose **Groovy**.
3) Load the file `TP02_tracking_script.groovy`.
4) Edit the two variables at the top:
   - `inputPath` → absolute path to your `cell2D_timelapse.tif`
   - `outDir` → absolute path to an output folder (existing)
5) Click **Run**.

Outputs:
- `tracking_results.xls` (ROI Statistics per track)
- `trackManager.xml` (serialized TrackManager content)
- A saved `.xml` sequence with ROIs and tracks for re‑opening in ICY

## B. With the **Protocol Editor (blocks)**
Create blocks in this order and connect outputs (sequence/ROI) accordingly:
1. **Sequence input**
   - path = your `cell2D_timelapse.tif`
2. **Wavelet Spot Detector Block**
   - Detector: UDWTWaveletDetector
   - Bright over dark = true
   - Scales: 1 and 2
   - Sensitivity: 100
   - Output: Export to ROI = true, Export to SwimmingPool = true
3. **Spot Tracking (Kalman / MHT)**  (name may vary: *Spot Tracking*, *MHT Tracking*)
   - Target motion: diffusive
   - Linking distance: 5 px
   - Gap closing: 1
   - Export to Track Manager = true
4. **ROI track statistics** (or Track Measurements)
   - Stats: Length, Duration, Mean velocity
5. **Track XLS export**
   - filename: tracking_results.xls
6. **Track XML export** (optional)
   - filename: trackManager.xml

Save the protocol (`File → Save`) to produce your `.icy` file.