# Ai 婚纱影像 Pro v2｜导演、表演、Camera Geometry 与商业组片

本模块吸收 LIRA / ACTING / CINEDANCE 的专业方法，但只采用可迁移原则；特定外部平台模型路由、固定视场角、固定 Prompt 语言等不覆盖本项目 Canon。

## 1. DIRECTOR_SYSTEM_4_LAYER

正式导演系统分四层：

1. `STORY_DIRECTION`｜当前 Scene / Shot 为什么存在
2. `PERFORMANCE_DIRECTION`｜人物为什么这样行动、如何听、如何反应
3. `PHYSICAL_CINEMATOGRAPHY_DIRECTION`｜Blocking、空间、Camera、Light、Physics
4. `MODEL_PROMPT_COMPILER`｜把已批准导演意图无损翻译成当前模型可执行语言

Prompt Engineering 是执行层，不代替策划、导演、表演和摄影判断。

## 2. SCENE_INTENT_CARD

叙事 Scene/Sequence 进入镜头设计前，按需要记录：

`story_purpose / dramatic_question / bride_objective / groom_objective / obstacle / stakes / relationship_in / relationship_out / information_change / emotion_in / emotion_out / visual_thesis / scene_end_state`

VF02/VF03 等叙事内容优先使用；VF01、纯婚纱肖像、视觉诗等不强制制造冲突，只需要明确视觉/关系/情绪目的。

## 3. PERFORMANCE_DIRECTION_SYSTEM

核心原则：表演写**可观察行为**，不让“浪漫、开心、难过、紧张”替代人物动作。

叙事表演按需要管理：

- `Objective`：当前人物想从具体对象获得什么，用动作动词描述；
- `Obstacle / Stakes`：什么阻碍它，失败代价是什么；
- `Tactic`：人物当前用什么办法推进；
- `Beat`：策略、信息、权力或关系发生变化的最小行动单元；
- `Subtext`：台词表层之外的真实目的；
- `Listening / Reaction`：听者在对方行动/台词进行中持续接收并反应；
- `Eye Life / Breath / Business / Proxemics / Status`：让人物有连续身体生命。

`BEAT != SHOT`：一个 Beat 可以由多个 Shot 表达；换机位不自动等于剧情变化。

## 4. PERFORMANCE_BEAT_MAP

视频或高叙事摄影可以记录：

`beat_id / objective / tactic / trigger / behavior_before / behavior_change / behavior_after / gaze / eyes / head / breath / hands / body / distance / dialogue / subtext / end_state`

不需要的字段可以省略，不能为了填表制造不存在的戏。

## 5. EYE_LIFE_REQUIRED

AI 人物最容易出现“眼睛死掉”。当前 Shot 需要时管理：

`GAZE_TARGET / MICRO_SACCADE / BLINK_STATE / GAZE_SHIFT / EYE_BEFORE_HEAD / CATCHLIGHT / ATTENTION_CHANGE`

自然情况下执行 `EYES_LEAD_HEAD`：眼睛先发现并落到目标，头部再跟随，肩线最后可能变化。

但 Eye Life 不是要求人物不停眨眼、扫视或表演；受控静止也可以是自然状态。

## 6. LISTENING_REACTION_RULE

有双人/多人互动时，听者不能等对方台词结束后才突然“切表情”。可以出现：

`关键词进入 → 眼神/呼吸变化 → 手部或 Business 停顿 → Assessment → 决定如何回应`

重大信息后允许 `ASSESSMENT_BEAT`。强事件后的身体与情绪残留执行 `EMOTIONAL_INERTIA`，不能下一镜自动恢复默认漂亮表情。

## 7. CHARACTER_BUSINESS / PROXEMICS / STATUS

人物可以正在整理头纱、拿花、写信、整理袖口、翻书、摆杯子、抚摸宠物等真实小任务；`INTERRUPTED_ACTION_ACCENT` 可以用“动作突然停住”表达事件发生。

双人距离是关系变量：记录 `COUPLE_DISTANCE_START / COUPLE_DISTANCE_END / WHO_CLOSES_DISTANCE / WHO_WITHDRAWS / WHO_STOPS`，但只在当前镜头真的需要时使用。

多人反应默认错开，不机械同步。婚纱静态肖像也可以只捕捉一个自然 `PERFORMANCE_MOMENT`，不需要完整戏剧 Beat。

## 8. PHOTO_POSE → PERFORMANCE_MOMENT

照片 Pose 不能只保存“牵手/拥抱/回眸”名称。正式 Shot 至少考虑：

`左右 / 前后 / 深度 / 距离 / BODY_ORIENTATION / SHOULDER_LINE / HIP_LINE / WEIGHT_LEG / HAND_ACTION / CONTACT_POINT / HEAD_DIRECTION / CHIN / GAZE / EXPRESSION / ACTION_PHASE`

Action Phase 基础为 `PRE / MID / PEAK / RELEASE`。自然婚纱摄影优先 MID/RELEASE，避免全部落在僵硬动作峰值。

照片可以截取动作过程中的真实瞬间，例如：眼睛刚移开、嘴角尚未完全展开、手正在整理裙摆，而不是每张都摆到动作终点。

## 9. DIR01｜摄影导演方案

DIR01 是结构化逻辑执行资产，不新增人物身份图片槽位。

AB04/AB05/AB06 等当前生产资产就绪后，照片批量生产前建立 DIR01：

`DIRECTOR_MODE / EMOTIONAL_ARC / SHOT_SCALE_LANGUAGE / COMPOSITION_LANGUAGE / ACTION_FAMILIES / GAZE_LANGUAGE / PROP_STRATEGY / CAMERA_LANGUAGE / LIGHTING_LANGUAGE / COLOR_LANGUAGE / SEQUENCE_RHYTHM`

DIR01 可以冻结并版本化；没有 DIR01 / Shot List / Coverage Preflight，不进入正式大批量 Photo Production。

## 10. PHOTO SHOT CONTROL CARD

照片 Shot 至少管理：

`SHOT_ID / SHOT_ROLE / SCENE_ZONE / DIRECTOR_MODE / SHOT_SCALE / ASPECT_RATIO / COMPOSITION / CAMERA_DIRECTION / CAMERA_HEIGHT / CAMERA_DISTANCE / CAMERA_PITCH / BRIDE_POSITION / GROOM_POSITION / COUPLE_DISTANCE / BODY_ORIENTATION / WEIGHT / HAND_INTERACTION / CONTACT_POINT / HEAD_DIRECTION / GAZE_RELATION / EXPRESSION / EMOTION_INTENSITY / ACTION / ACTION_PHASE / PROP / PROP_INTERACTION / FOCUS_TARGET`

Shot Role：`Hero / Support / Detail / Safety`。

## 11. SHOT_DIVERSITY_GATE

商业套系不允许一个构图/姿势/表情复制几十次。

Coverage 根据最终照片数量动态规划：环境大景、环境全身、全身、七分身、半身、近景、特写、横版、竖版、静态、动态、看镜头、不看镜头、单人、双人、多机位、多动作、不同视线关系和必要道具。

曾提出的“10 张以上单一构图/姿势/景别/机位约不超过 30%”只作为默认软警戒，不是不可突破的数学硬门；明确连续动作 Sequence、极简固定机位方案或用户创意允许有理由偏离。

## 12. PROP_DIRECTION

道具不是为了覆盖率硬塞。只有它对造型、互动、文化、剧情或画面平衡有明确作用时使用。

Prop 至少记录：`PROP_ID / OWNER / POSITION / HOLDING_HAND / CONTACT_POINT / INTERACTION / ALLOW_PASS_BETWEEN_PERSONS / STATE_BEFORE / STATE_AFTER`。

宠物属于独立身份主体，不能因主题名称擅自改品种、体型、毛色或结构。

## 13. BLOCKING_BEFORE_FRAMING

正式顺序：

`人物意图/动作 → 人物站位/路线 → 双人距离/接触 → Scene Geography → Camera Station → Framing/Optics → Motion`

不要先选一个“漂亮机位”，再强行让人物迁就它。

## 14. Scene Geography / Camera Station

复杂 Scene 按需要维护：门、窗、家具、道路、主要道具、人物安全站位、前中后景、移动路线、180°轴和 `CAM-A/B/C...`。

Scene 多视图遵守 `Same World, Different Camera`：换 Camera，不换建筑、家具和固定物体位置。

## 15. FIRST_FRAME / END_STATE

视频 Shot 必须管理 `FIRST_FRAME_CONTRACT` 与 `END_STATE_CONTRACT`。

第一帧明确人物是否已经出现、屏幕位置、世界位置、身体朝向、视线、道具、Camera Side 和光线。

结束状态保存人物位置、身体方向、视线、手部/道具、运动方向、Camera、Light、Audio 和 Performance State，作为下一 Shot 的 Continuity 输入。

## 16. Camera Geometry

分别管理：

`shot_size / camera_distance / camera_azimuth / camera_height / camera_pitch / camera_roll / camera_aim_point / focal_length_or_optical_intent / composition / subject_occupancy / aspect_ratio`

必须区分：

- 景别 ≠ Camera Distance
- 机位高度 ≠ Pitch
- Camera Position ≠ 人物身体方向
- `HEAD_VIEW_DIRECTION` ≠ `BODY_ORIENTATION`
- `BODY_DIRECTION` ≠ `GAZE_DIRECTION`

## 17. OPTICAL_OUTCOME_FIRST

内部可以规划 Camera Body / Sensor / Lens / Actual Focal / Equivalent Focal / Aperture / Shutter / ISO / WB / Focus / Exposure，但模型 Prompt 不机械堆假 EXIF。

`Camera-to-Rendering Compiler` 优先翻译成可见结果：

`透视 / 空间压缩 / 景深 / 焦平面 / 主体与背景距离感 / 动作冻结或拖影 / 高光 / 暗部 / 肤质 / 面料 / 空间层次`

例如中长焦应写出人物比例稳定、背景压缩、Camera 与主体实际距离和渐进景深，而不仅是一句“85mm”。外部 Skill 的固定 FOV 度数库只作为知识参考，不成为小云雀硬参数。

## 18. CAMERA_MOTION_CARD

视频 Camera Movement 记录：

`start_position / end_position / start_scale / end_scale / trajectory / speed / acceleration / target / stabilization / focus_behavior / motivation`

`NO_RANDOM_CAMERA_MOVEMENT`：运动必须有叙事、情绪或空间动机；没有动机时优先锁机位。

一个 Beat 原则上只有一个主要 Camera Behavior，除非导演明确设计复杂一镜到底。

## 19. MOTION_PHYSICS_ENGINE

动作至少考虑：`gravity / mass / inertia / friction / contact / weight_transfer / acceleration / deceleration / follow_through / fabric_delay / hair_delay / liquid_or_particle_response`。

婚纱重点检查：高跟鞋脚地接触、裙摆重量、拖尾、头纱延迟、发丝风向、花束重量、人物牵手/拥抱接触、椅子/台阶支撑、宠物真实身体结构。

禁止漂浮、滑行、瞬移、穿模、橡胶身体、无重量布料和道具。

## 20. LIGHTING_PRIORITY_LOCK

灯光不是“风格装饰”。正式 Lighting Asset 至少记录：

`KEY_SOURCE / DIRECTION / CAMERA_RELATION / SUBJECT_SHADOW_SIDE / FILL / RIM_OR_ENVIRONMENT / QUALITY / INTENSITY_RELATION / COLOR_TEMPERATURE / BACKGROUND_LEVEL / EXPOSURE_PRIORITY / SHADOW_DIRECTION / ALLOWED_CHANGE`

标准人物资产阶段继续执行中性光；正式 Shot 才允许创意摄影光。

## 21. MOTIVATED_FILMMAKING

每一个动作、Camera Movement、Transition、Prop 和 Sound 都应该回答“为什么现在需要它”。没有原因时，不为了“电影感”强行增加 Orbit、Whip、光斑、慢动作或复杂转场。

## 22. PRODUCTION_CONTROL_ASSETS

以下均可独立进入完整状态机并冻结：

`BLOCKING-ASSET / STORYBOARD-ASSET / CAMERA-ASSET / LIGHTING-ASSET / MOTION-ASSET / AUDIO-CUE-ASSET / DIR01`

已冻结后，后续 Prompt 不重新设计它们，只描述未锁定或 Delta；如果当前模型没有直接读取这些内部资产的能力，Prompt Compiler 按 `REFERENCE_BINDING_TRUTH` 展开该 Shot 已批准的执行信息。
