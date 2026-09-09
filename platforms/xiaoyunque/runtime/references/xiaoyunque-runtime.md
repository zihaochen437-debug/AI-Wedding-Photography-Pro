# 小云雀 Runtime｜原生结构、工具、模型、自由画布与能力真实性

## 1. 当前发行范围

当前版本只针对小云雀。豆包、扣子及其他平台规则属于历史资料，不参与 Runtime 决策。

## 2. 原生 Compact Runtime

优先“小云雀原生 Skill”结构：

`SKILL.md + references/INDEX.md + 少量高密度 references`

开发层 M00–M18、Active Canon、测试、迁移、Schema/Registry 可以在 Source Archive 保留，但不要求在 Runtime 中一一对应物理文件。

原则：

**可以压缩文件，不能压缩能力。**

## 3. XIAOYUNQUE_PACKAGE_POLICY

正式包禁止脚本和可执行文件。至少不得包含：

`.py / .pyc / .sh / .bat / .cmd / .ps1 / .exe`

不包含 `scripts/`。

开发构建工具、测试、Archive、Migration Report、其他平台 Adapter 不进入运行包。

历史实测曾出现 `too_many_files`；因此 Runtime 保持紧凑，不宣称一个未经官方确认的精确文件上限。

## 4. Frontmatter

遵循用户提供的小云雀原生 Skill 样本：

- `name`：英文机器标识
- `display_name`：中文显示名称
- `description`：能力 + 触发条件
- `tools`：仅声明观察到的小云雀原生工具入口

本版显示名称：`Ai 婚纱摄影 Pro`

本版 tools 声明：

- `sandbox_generate_image`
- `sandbox_generate_video`
- `sandbox_process_video`
- `render_video`

这些名称来自用户提供的小云雀原生 Skill 样本；仍须在当前运行时实际调用成功后，才能对具体动作标记 `AGENT_DIRECT_CALLABLE = VERIFIED`。

## 5. 能力真实性

证据状态：

- `XYQ_DIRECT`：小云雀官方/界面直接确认
- `USER_VERIFIED`：用户实测确认
- `SEED_OFFICIAL`：字节 Seed 官方存在，但未证明当前小云雀账号开放
- `RUNTIME_UNKNOWN`：当前账号/权限/版本/限额未知

调用层：

- `UI_AVAILABLE`
- `USER_INTERACTIVE`
- `AGENT_DIRECT_CALLABLE`

这几项不能互相推导。

看到自由画布“超分/扩图/局部重绘/打光/镜头/图层”等按钮，只能说明 UI 能力存在；未经实测不得说 Skill Agent 已经自动调用。

## 6. 动态模型角色

内部按能力角色路由：

- `REASONING_MODEL`
- `IMAGE_IDENTITY_MODEL`
- `IMAGE_CREATIVE_MODEL`
- `IMAGE_EDIT_MODEL`
- `IMAGE_SCENE_MODEL`
- `VIDEO_SHOT_MODEL`
- `VIDEO_SEQUENCE_MODEL`
- `VIDEO_EDIT_MODEL`
- `AUDIO_MODEL`（仅实际可用时）

模型名称和版本不永久写死。

字节官方存在某模型 ≠ 当前小云雀账号可用。当前运行时不显示模型时记录 `UNKNOWN`。

用户不需要每个 Shot 重新选择模型；采用阶段级 Model Plan，只在模型切换、不可用、能力/成本/隐私变化或用户要求时重新确认。

## 7. 自由画布

已观察到的一级模块可包括：角色、场景、3D导演台、多轨编辑器、视频、图片、文本、音频。

已观察到的图片/编辑类能力可包括：模型选择、风格库、比例/清晰度、预设提示词、妆容/表情/人像质感、打光、镜头、超分、局部重绘、图层分离、裁剪、旋转、抠图、扩图、解析等。

但：

**自由画布 UI 能力 ≠ Skill Agent 自动调用能力。**

3D导演台可以作为人物站位、动作、空间、机位和运动关系的可视化导演工具；没有实测的坐标、骨骼、路径或接口参数不得自行编造。

## 8. 4K 与输出规格

小云雀界面中的 1K/1.5K/2K/4K 等属于平台可选质量/规格层。4K 不自动等于一个固定宽×高，也不等于某模型的 API 原生像素事实。

运行时记录：

`REQUESTED_QUALITY / REQUESTED_RATIO / REQUESTED_SIZE / ACTUAL_NATIVE_SIZE / UPSCALE_USED / FINAL_OUTPUT_SIZE`

生成比例控制 ≠ 后期裁剪。目标产品是竖屏/横屏时优先按目标比例生成。

## 9. Persistence Truth

如果当前小云雀环境能真实保存项目状态，标记 `PERSISTED`；只能依赖当前会话则 `SESSION_ONLY`；无法确认则 `UNKNOWN`。

最小状态需要维护：

project_id、current_phase、current_active_task、reference_intake_status、AB01–AB06 状态、current_suite/look/scene、approved_storyboard/camera/lighting/motion、photo_target_count、video_projects、active_generation_refs、last_approved_asset、open_revision、model_plan、persistence_status。

如果无法真正持久化，不得声称“已永久保存”。

## 10. 平台失败回退

工具/模型不可用时：

1. 明确说明当前能力状态；
2. 不虚构已经执行；
3. 保留业务规则和 Prompt/资产计划；
4. 如属于 UI 可交互能力，给用户最短可执行操作；
5. 继续维护状态，避免重新策划已批准内容。
