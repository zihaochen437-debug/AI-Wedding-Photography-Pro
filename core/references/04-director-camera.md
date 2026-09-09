# 摄影导演、Camera Geometry 与商业组片

## 1. Blocking / Pose

正式 Shot 内部至少考虑：左右、前后、深度、距离、身体方向、肩、骨盆、重心腿、左右手、接触点、头部、下巴、视线、表情与 Action Phase。

Action Phase：`PRE / MID / PEAK / RELEASE`；自然婚纱摄影优先 MID/RELEASE，避免所有镜头都落在僵硬峰值。

## 2. Camera Geometry

分别管理：`shot_size / camera_distance / camera_azimuth / camera_height / camera_pitch / camera_roll / camera_aim_point / focal_length / composition / subject_occupancy / aspect_ratio`。

景别 ≠ 摄影距离；机位高度 ≠ Pitch；摄影机位置 ≠ 人物身体朝向。

## 3. 摄影器材与曝光意图

内部可规划 Camera Body / Sensor / Lens / Actual Focal / Equivalent Focal / Aperture / Shutter / ISO / WB / Focus / Exposure，但模型 Prompt 不机械堆假 EXIF。

`Camera-to-Rendering Compiler` 将这些意图翻译成可见结果：透视、空间压缩、景深、焦平面、动作冻结/轻微动态、高光、暗部、肤质、婚纱/西装材质、空间层次。不得声称 AI 图真实由某台实体相机拍摄或伪造 RAW/EXIF。

## 4. 商业组片

固定层级：`Scene → Look → Sequence → Shot`。

Shot 角色：`Hero / Support / Detail / Safety`。

根据目标数量动态覆盖：环境大景、环境全身、全身、七分身、半身、近景、特写、横版、竖版、静态、动态、看镜头、不看镜头、单人、双人、多机位、多动作。不能一个构图复制几十次。

## 5. 生产控制资产

`BLOCKING-ASSET / STORYBOARD-ASSET / CAMERA-ASSET / LIGHTING-ASSET / MOTION-ASSET / AUDIO-CUE-ASSET` 均可进入完整状态机并冻结。已冻结后，后续 Prompt 不重新设计它们，只描述未锁定或 Delta。
