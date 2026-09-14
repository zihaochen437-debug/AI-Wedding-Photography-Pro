# Ai 婚纱影像 Pro v2｜小云雀模型 Catalog 与 Runtime 路由

本文件用于小云雀 Runtime。完整模型目录必须保留，但“目录存在”与“当前账号可调用”严格分离。

## 1. 状态字段

每个模型至少记录：

`MODEL_NAME / MODEL_ROLE / EVIDENCE_STATUS / MODEL_AVAILABLE / UI_AVAILABLE / USER_INTERACTIVE / AGENT_DIRECT_CALLABLE / VERIFIED_AT / NOTES`

允许的证据：`XYQ_DIRECT / XYQ_SERVICE / USER_VERIFIED_RUNTIME / SEED_OFFICIAL / BYTEPLUS_OFFICIAL / RUNTIME_UNKNOWN`。

硬规则：ByteDance 官方存在某型号 ≠ 当前小云雀账号开放；UI 可见 ≠ Skill Agent 可直接调用。

## 2. 推理 / 思考模型池

必须保留：

- Seed2.1 Pro
- Seed2.1 Turbo
- Seed2.0 Pro
- Seed2.0 Lite
- Seed2.0 Mini
- Seed1.8
- Seed1.6
- Seed1.5-VL
- Seed1.5 / Doubao-1.5-pro

当前小云雀若不显示实际推理型号，记录：

`reasoning_model: UNKNOWN`
`selection_source: PLATFORM_DEFAULT`

不得根据模型能力宣传或旧资料猜测后台实际使用型号。

## 3. 图片模型池

必须保留：

- Seedream 5.0 Pro
- Seedream 5.0 Lite
- Seedream 4.5
- Seedream 4.0
- SeedEdit 3.0
- Anycook 影视版
- Anycook 标准版
- Anycook 创意版
- 旗舰生图 V2-Pro
- 即梦AI 图片生成 4.6
- 即梦文生图 3.1
- 即梦文生图 3.0
- 即梦图生图 3.0 智能参考

项目历史中小云雀界面曾实测看到 Seedream 5.0 Pro、Anycook 三版本和旗舰生图 V2-Pro；保留 `USER_VERIFIED_RUNTIME` 历史证据，但每个新项目仍需 Preflight 当前是否可见/可用。

Seedream 当前规格属于版本化证据，不能写成永久常量：历史核验中 5.0 Pro 为 1K/2K、5.0 Lite 为 2K/3K/4K、4.5 为 2K/4K、4.0 为 1K/2K/4K；运行时以最新实际平台选项与官方资料为准。

### 图片角色

- `IMAGE_IDENTITY_MODEL`：人物 M/U/F/D、双人比例、身份高风险任务
- `IMAGE_CREATIVE_MODEL`：婚纱创意、故事 Look、道具、风格探索
- `IMAGE_EDIT_MODEL`：局部改妆、手部/服装/Scene Scoped Revision
- `IMAGE_SCENE_MODEL`：Scene Base、多视角场景、空场景
- `IMAGE_KEYFRAME_MODEL`：Storyboard、Opening/Ending Frame、Bridge Keyframe

不得写死“最高版本处理所有角色”。每个阶段以身份稳定、编辑能力、当前质量、成本和实际可用性路由。

## 4. 视频模型池

必须保留：

- Seedance 2.5
- Seedance 2.0
- Seedance 2.0 Mini
- Seedance 2.0 Fast / fast 720p
- Seedance 1.5 Pro
- Seedance 1.0

### 推荐任务路由

- `VIDEO_SHOT_MODEL`：Seedance 2.5 为正式优先候选；关键 Hero、人物表演、复杂 Camera 以实际 A/B 结果确定。
- `VIDEO_SEQUENCE_MODEL`：Seedance 2.5 为 10–30s 连续段落候选；模型上限不等于每段都生成 30s。
- `VIDEO_EDIT_MODEL`：优先使用当前小云雀真实开放的 Seedance 视频编辑/定向重绘/延长能力；未验证时不得声称可自动调用。
- Seedance 2.0：多模态参考和 2.5 备用。
- Seedance 2.0 Fast/Mini：若可用，优先 Previz、动作和节奏测试，不自动作为最终商业母片。
- Seedance 1.5 Pro / 1.0：只在实际任务有优势或兼容需要时使用，不因旧版经验自动优先。

Seedance 2.5 官方存在 30s 级单次生成、多模态参考、延长和定向编辑等能力；当前小云雀具体入口、限额、分辨率与 Agent 调用必须单独 Preflight。

## 5. 视频专项服务池

保留：

- 即梦AI 视频生成 3.0 Pro
- 即梦AI 视频 3.0 1080P / 720P
- 动作模仿 2.0
- OmniHuman 1.5
- OmniHuman 1.0 快速模式
- 视频翻译 2.0
- 字幕擦除

这些是专项服务，不自动等同 Seedance 模型家族。

## 6. 音频 / 语音 / 音乐模型池

保留：

- Seed Audio 1.0
- Seed-Music
- SeedRealtime
- Seeduplex
- Seed LiveInterpret 2.0
- Seed Realtime Voice

Seed Audio 1.0 的 100ms 级对白时序能力属于官方模型事实；是否能被当前小云雀 Skill 直接调用仍为 `RUNTIME_UNKNOWN`，除非当前项目实测成功。

影视生产规则高于模型便利性：Picture Lock 前不生成非剧情背景音乐；VOICEOVER 默认后期加入。

## 7. 3D / 空间预演

保留：

- Seed3D 2.0
- Seed3D 1.0
- 小云雀 3D导演台
- 小云雀多轨编辑器

3D导演台用于 Blocking、Scene Geography、Camera Station/Path、道具尺度和空间预演。只使用当前界面/实测真实能力，不编造坐标、骨骼或 API 参数。

## 8. 阶段级 MODEL_PLAN

一个项目至少记录：

```yaml
model_plan:
  reasoning:
    model:
    runtime_status:
  identity_image:
    model:
    runtime_status:
  creative_image:
    model:
    runtime_status:
  image_edit:
    model:
    runtime_status:
  scene_image:
    model:
    runtime_status:
  video_shot:
    model:
    runtime_status:
  video_sequence:
    model:
    runtime_status:
  video_edit:
    model:
    runtime_status:
  audio_post:
    model:
    runtime_status:
  previs_3d:
    tool:
    runtime_status:
```

每次模型切换记录：`why_selected / references / prompt_version / failure_reason / switch_reason`。

## 9. Runtime Preflight

在以下节点重新确认当前小云雀能力：

1. 首张正式 M01 生图前；
2. 首次 AB04/AB05/AB06 正式生成或编辑前；
3. VF01/VF02/VF03 正式生产前；
4. 第一次视频编辑、延长或音频后期前；
5. 模型失败、限额、入口变化或用户要求切换时。

未实测的能力始终标记 `UNKNOWN`，不能把 Catalog 当成当前可用列表。