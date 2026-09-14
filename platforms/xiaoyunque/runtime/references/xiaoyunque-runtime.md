# Ai 婚纱影像 Pro v2｜小云雀 Runtime、工具、模型、自由画布与能力真实性

## 1. 当前发行范围

当前 v2 第一优先 Runtime 只针对 **小云雀**。豆包及其他平台属于历史/未来 Adapter 资料，不参与当前小云雀生产决策。

Universal Core 继续平台无关，平台约束只进入 Adapter/Runtime。

## 2. Compact Runtime

采用：

`SKILL.md + references/INDEX.md + 少量高密度 references`

原则：**可以压缩文件，不能压缩业务能力。**

开发层 Active Canon、测试、研究、Schema、Catalog、迁移资料可以保留在 Source Repository，但不要求全部进入小云雀运行包。

## 3. XIAOYUNQUE_PACKAGE_POLICY

正式小云雀包禁止脚本和可执行文件，至少不得包含：

`.py / .pyc / .sh / .bat / .cmd / .ps1 / .exe`

不包含 `scripts/`。历史实测出现过 `too_many_files`，因此 Runtime 保持紧凑，不虚构未经官方确认的精确文件数量上限。

## 4. Frontmatter

遵循已观察到的小云雀原生 Skill 结构：

- `name`：机器标识，可为历史兼容保留 `ai-wedding-photography`
- `display_name`：v2 用户可见名称必须是 `Ai 婚纱影像 Pro`
- `description`：能力 + 触发条件
- `tools`：只声明已观察到的小云雀原生工具入口

当前 tools 声明：

- `sandbox_generate_image`
- `sandbox_generate_video`
- `sandbox_process_video`
- `render_video`

工具名称来自小云雀原生 Skill 样本；具体动作仍须实际调用成功才能标记 `AGENT_DIRECT_CALLABLE=VERIFIED`。

## 5. Capability Truth

证据层：

- `XYQ_DIRECT`
- `XYQ_SERVICE`
- `USER_VERIFIED_RUNTIME`
- `SEED_OFFICIAL`
- `BYTEPLUS_OFFICIAL`
- `RUNTIME_UNKNOWN`

调用层：

- `MODEL_AVAILABLE`
- `TOOL_AVAILABLE`
- `UI_AVAILABLE`
- `USER_INTERACTIVE`
- `AGENT_DIRECT_CALLABLE`

这些状态不能互相推导。

例如自由画布出现超分、扩图、局部重绘、打光、镜头或图层按钮，只能证明相应 UI 能力存在；未经 Agent 调用实测，不得说 Skill 已经自动完成。

## 6. 模型治理

完整候选目录见 `model-catalog.md`。

模型职责：

`REASONING_MODEL / IMAGE_IDENTITY_MODEL / IMAGE_CREATIVE_MODEL / IMAGE_EDIT_MODEL / IMAGE_SCENE_MODEL / IMAGE_KEYFRAME_MODEL / VIDEO_SHOT_MODEL / VIDEO_SEQUENCE_MODEL / VIDEO_EDIT_MODEL / AUDIO_POST_MODEL / PREVIS_3D_TOOL`

不永久写死具体型号。每个项目维护阶段级 `MODEL_PLAN`；关键生成、视频、编辑、音频节点执行 Runtime Preflight。

用户不需要每个 Shot 重新选模型；只在不可用、受控 A/B 证据、成本/隐私/质量要求变化或用户要求时切换。

## 7. 自由画布

当前已观察到的一级模块包括角色、场景、3D导演台、多轨编辑器、视频、图片、文本、音频等。

图片/编辑侧已观察到的能力可包括模型选择、风格、比例/清晰度、预设提示、妆容/表情/人像质感、打光、镜头、超分、局部重绘、图层分离、裁剪、旋转、抠图、扩图、解析等。

**UI 能力 ≠ Agent 自动调用能力。**

3D导演台可用于 Blocking、Scene Geography、Camera Station/Path 和空间预演；没有实测的坐标、骨骼、路径或接口参数不得编造。

## 8. 输出规格

小云雀界面中的 1K/1.5K/2K/4K 等属于平台当前质量/规格层。4K 不自动等于固定宽×高，也不自动等于底层模型 API 原生像素事实。

记录：

`REQUESTED_QUALITY / REQUESTED_RATIO / REQUESTED_SIZE / ACTUAL_NATIVE_SIZE / UPSCALE_USED / FINAL_OUTPUT_SIZE`

人物正确性 > 像素档位。目标产品比例优先在生成阶段规划，不把后期裁剪当成全部构图问题的补救。

## 9. PROJECT_STATE_SNAPSHOT

最小快照必须能恢复 v2 当前生产位置，而不是只写“AB01 已完成”。至少维护：

```yaml
project_id:
project_version:
current_phase:
current_active_task:
persistence_status:

reference_intake_status:
retouch_profile:
standard_wardrobe:

identity_assets:
  bride: {M01: null, U01: null, F01: null, D01: null}
  groom: {M01: null, U01: null, F01: null, D01: null}
  couple: {C01: null}

phase_b:
  work_mode:
  output_type:
  photo_target_count:
  current_suite:
  current_look:
  current_scene:

creative_assets:
  AB04:
  AB05:
  AB06:
  DIR01:
  approved_camera:
  approved_lighting:
  approved_motion:

film_projects:
  - video_id:
    product_class:
    story_autonomy:
    storyboard_autonomy:
    story_status:
    VP01:
    VS01:
    VD01:
    VC01:
    VB01:
    VSL01:
    VA01:
    EDL01:
    picture_lock:
    film_qc_status:

active_generation_refs:
qc_audit_refs:
last_approved_asset:
open_revision:
model_plan:
```

如果小云雀不能真实保存这些状态，仍可在当前会话逻辑维护，但必须标 `SESSION_ONLY` 或 `UNKNOWN`，不得谎称永久持久化。

## 10. Persistence Truth

- `PERSISTED`：真实保存并通过恢复测试
- `SESSION_ONLY`：只在当前会话/当前项目运行态可靠
- `UNKNOWN`：无法确认

“自由画布中仍然看得到”本身不足以证明跨会话、跨设备或长期存储能力。

## 11. Recovery

恢复项目时：

`Load Snapshot → Validate Frozen Authority → Check Dependency Health → Resolve Open Revision → Resume Current Gate`

不得因为新会话重新规划已经批准的 Story、Look、Scene、DIR01、VB01 或 Shot。

若状态冲突，以用户当前确认、最新有效资产版本和可验证平台状态为准，冲突项标记 `NEEDS_REVALIDATION`。

## 12. 运行失败回退

工具/模型不可用时：

1. 明确当前 capability status；
2. 不虚构已经执行；
3. 保留业务规则、Prompt、资产与 Film Plan；
4. 若属于 UI 可交互能力，给用户最短操作路径；
5. 维护当前 Snapshot，避免重新策划已批准内容；
6. 只有存在可验证替代模型/工具时才执行 fallback，并记录 `switch_reason`。
