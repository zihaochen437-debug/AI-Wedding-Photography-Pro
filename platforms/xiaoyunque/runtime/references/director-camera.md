# Ai 婚纱影像 Pro v2｜导演、表演、Camera Geometry 与商业组片

本模块把 LIRA / ACTING / CINEDANCE 的可迁移方法婚纱化，不照搬其 Higgsfield 路由、固定视场角、固定英语 Prompt 等平台专属规则。

## 1. DIRECTOR_SYSTEM_4_LAYER

1. `STORY_DIRECTION`：当前 Scene/Shot 为什么存在
2. `PERFORMANCE_DIRECTION`：人物为什么这样行动、如何听、如何反应
3. `PHYSICAL_CINEMATOGRAPHY_DIRECTION`：Blocking、空间、Camera、Light、Physics
4. `MODEL_PROMPT_COMPILER`：把已批准导演意图无损翻译成小云雀当前模型可执行语言

Prompt Engineering 是执行层，不代替导演判断。

## 2. SCENE_INTENT_CARD

叙事 Scene/Sequence 按需要记录：

`story_purpose / dramatic_question / bride_objective / groom_objective / obstacle / stakes / relationship_in / relationship_out / information_change / emotion_in / emotion_out / visual_thesis / scene_end_state`

VF02/VF03 优先使用。VF01、静态婚纱肖像、纯视觉诗不强制制造冲突，只明确视觉、关系、状态或情绪目的。

## 3. PERFORMANCE_DIRECTION_SYSTEM

表演写可观察行为，不用“浪漫、开心、难过、紧张”替代动作。

叙事场景按需要管理 `Objective / Obstacle-Stakes / Tactic / Beat / Subtext / Listening / Reaction / Eye Life / Breath / Business / Proxemics / Status`。

`BEAT != SHOT`：换机位不自动等于剧情 Beat 改变。

## 4. Eye Life / Listening

需要时管理：`GAZE_TARGET / MICRO_SACCADE / BLINK_STATE / GAZE_SHIFT / EYE_BEFORE_HEAD / CATCHLIGHT / ATTENTION_CHANGE`。

默认自然规律：眼睛先发现目标，头部随后跟随；受控静止也是正常表演，不要求人物不停眨眼或扫视。

有双人对白/互动时，听者在对方动作/台词进行中持续反应；重要信息后允许 Assessment Beat。强事件后的状态跨镜具有 `EMOTIONAL_INERTIA`。

## 5. Character Business / Distance / Status

人物可以整理头纱、拿花、写信、整理袖口、翻书、摆杯子、抚摸宠物等；动作突然停止可作为事件标点。

需要时记录双人距离变化、谁靠近/后退/停下。多人/双人反应默认不机械同步。

## 6. PHOTO_POSE → PERFORMANCE_MOMENT

照片 Shot 不只保存“牵手/拥抱/回眸”名称。至少考虑：

`左右 / 前后 / 深度 / 距离 / BODY_ORIENTATION / SHOULDER_LINE / HIP_LINE / WEIGHT_LEG / HAND_ACTION / CONTACT_POINT / HEAD_DIRECTION / CHIN / GAZE / EXPRESSION / ACTION_PHASE`

Action Phase：`PRE / MID / PEAK / RELEASE`。自然婚纱摄影优先 MID/RELEASE，允许截取真实动作中间态。

## 7. DIR01｜摄影导演方案

DIR01 是逻辑执行资产，不新增人物标准图片。

正式照片批量生产前建立：

`DIRECTOR_MODE / EMOTIONAL_ARC / SHOT_SCALE_LANGUAGE / COMPOSITION_LANGUAGE / ACTION_FAMILIES / GAZE_LANGUAGE / PROP_STRATEGY / CAMERA_LANGUAGE / LIGHTING_LANGUAGE / COLOR_LANGUAGE / SEQUENCE_RHYTHM`

DIR01、Shot List、Coverage Preflight 未就绪时不进入正式批量 Photo Production。

## 8. PHOTO SHOT CONTROL CARD

至少管理：

`SHOT_ID / SHOT_ROLE / SCENE_ZONE / DIRECTOR_MODE / SHOT_SCALE / ASPECT_RATIO / COMPOSITION / CAMERA_DIRECTION / CAMERA_HEIGHT / CAMERA_DISTANCE / CAMERA_PITCH / BRIDE_POSITION / GROOM_POSITION / COUPLE_DISTANCE / BODY_ORIENTATION / WEIGHT / HAND_INTERACTION / CONTACT_POINT / HEAD_DIRECTION / GAZE_RELATION / EXPRESSION / EMOTION_INTENSITY / ACTION / ACTION_PHASE / PROP / PROP_INTERACTION / FOCUS_TARGET`

Shot Role：`Hero / Support / Detail / Safety`。

## 9. SHOT_DIVERSITY_GATE

商业套系不能一个构图/姿势/表情复制几十次。根据最终数量动态覆盖环境大景、全身、半身、近景、特写、横竖版、静态/动态、不同视线、单人/双人、动作、机位和必要道具。

“10张以上同一构图/姿势/景别/机位约不超过30%”仅为软警戒；明确连续动作 Sequence、极简方案或用户创意可有理由偏离。

道具不是为了覆盖率硬塞；只有造型、互动、文化、剧情或画面平衡需要时使用。

## 10. BLOCKING_BEFORE_FRAMING

顺序：

`人物意图/动作 → 站位/路线 → 双人距离/接触 → Scene Geography → Camera Station → Framing/Optics → Motion`

复杂 Scene 按需要维护门窗、家具、道具、前中后景、人物路线、180°轴和 Camera Station。

## 11. FIRST_FRAME / END_STATE

视频 Shot 管理 `FIRST_FRAME_CONTRACT` 与 `END_STATE_CONTRACT`。

第一帧明确人物、屏幕/世界位置、身体朝向、视线、道具、Camera Side 和光线。End State 保存人物位置、方向、视线、手/道具、运动、Camera、Light、Audio 和 Performance，供下一 Shot 继承。

## 12. Camera Geometry

分别管理：

`shot_size / camera_distance / camera_azimuth / camera_height / camera_pitch / camera_roll / camera_aim_point / focal_length_or_optical_intent / composition / subject_occupancy / aspect_ratio`

景别 ≠ 距离；机位高度 ≠ Pitch；Camera Position ≠ Body Direction；Head Direction ≠ Body Orientation ≠ Gaze。

## 13. OPTICAL_OUTCOME_FIRST

内部可规划 Camera Body / Sensor / Lens / Focal / Aperture / Shutter / ISO / WB / Focus / Exposure，但 Prompt 不堆假 EXIF。

优先描述可见结果：透视、背景压缩、景深、焦平面、Camera 与人物实际距离、动作冻结/动态、高光暗部、肤质、面料和空间层次。

外部 Skill 的固定 FOV 度数只作为参考知识，未在小云雀验证前不成为硬参数。

## 14. CAMERA_MOTION_CARD

视频 Camera Motion：

`start_position / end_position / start_scale / end_scale / trajectory / speed / acceleration / target / stabilization / focus_behavior / motivation`

`NO_RANDOM_CAMERA_MOVEMENT`：没有叙事、情绪或空间动机时优先不动；一个 Beat 原则上一个主要 Camera Behavior。

## 15. MOTION_PHYSICS_ENGINE

至少考虑 `gravity / mass / inertia / friction / contact / weight_transfer / acceleration / deceleration / follow_through / fabric_delay / hair_delay`。

婚纱重点：高跟鞋脚地接触、裙摆重量、拖尾、头纱、发丝、花束、牵手/拥抱、椅子/台阶、宠物身体结构。

## 16. LIGHTING_PRIORITY_LOCK

正式 Lighting Asset 至少记录：

`KEY_SOURCE / DIRECTION / CAMERA_RELATION / SUBJECT_SHADOW_SIDE / FILL / RIM_OR_ENVIRONMENT / QUALITY / INTENSITY_RELATION / COLOR_TEMPERATURE / BACKGROUND_LEVEL / EXPOSURE_PRIORITY / SHADOW_DIRECTION / ALLOWED_CHANGE`

标准人物资产继续中性光；正式 Shot 才允许创意灯光。

## 17. MOTIVATED_FILMMAKING

动作、Camera Movement、Transition、Prop、Sound 都应回答“为什么现在需要它”。没有原因时不为了所谓电影感强加 Orbit、Whip、慢动作或复杂转场。

## 18. PRODUCTION_CONTROL_ASSETS

`BLOCKING-ASSET / STORYBOARD-ASSET / CAMERA-ASSET / LIGHTING-ASSET / MOTION-ASSET / AUDIO-CUE-ASSET / DIR01` 均可版本化并冻结。

若小云雀不能把这些内部资产对象直接传给模型，Prompt Compiler 按 `REFERENCE_BINDING_TRUTH` 展开当前 Shot 已批准的执行信息，而不是只发送一个内部 ID。
