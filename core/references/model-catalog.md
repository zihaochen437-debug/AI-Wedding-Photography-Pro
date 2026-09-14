# Ai 婚纱影像 Pro v2｜完整模型与专项服务 Catalog

本文件记录项目已知候选模型/服务，不代表当前小云雀账号一定可调用。

最高规则：`MODEL_CATALOG_IS_COMPLETE_BUT_RUNTIME_DYNAMIC`。

## 1. Evidence Status

每条记录至少标记一个来源状态：

- `XYQ_DIRECT`：小云雀官方页面/界面直接确认存在
- `XYQ_SERVICE`：小云雀/剪映/火山关联服务文档确认
- `USER_VERIFIED_RUNTIME`：用户在真实小云雀界面/账号实测看到或使用过
- `SEED_OFFICIAL`：ByteDance Seed 官方确认
- `BYTEPLUS_OFFICIAL`：BytePlus/火山引擎官方确认
- `GITHUB_REFERENCE`：优质开源 Skill/工程参考，不等于平台能力
- `RUNTIME_UNKNOWN`：当前小云雀账号/权限/入口/限额尚未验证

存在性与调用能力分开记录：

`MODEL_AVAILABLE / UI_AVAILABLE / USER_INTERACTIVE / AGENT_DIRECT_CALLABLE`。

官方存在、界面可见、用户可手动使用、Skill Agent 可直接调用，四者不能互相推导。

## 2. 推理 / 思考 / 多模态理解模型

| 模型 | 项目角色 | 基础证据 | 小云雀当前调用状态 |
|---|---|---|---|
| Seed2.1 Pro | 总导演、复杂策划、剧本分析、全局 QC、复杂依赖与影视连续性 | SEED_OFFICIAL | RUNTIME_UNKNOWN |
| Seed2.1 Turbo | 日常交互、Prompt Compiler、资产路由、快速规划 | SEED_OFFICIAL | RUNTIME_UNKNOWN |
| Seed2.0 Pro | 复杂长链推理备用 | SEED_OFFICIAL | RUNTIME_UNKNOWN |
| Seed2.0 Lite | 图像/视频/音频/文本联合理解与素材审查 | SEED_OFFICIAL | RUNTIME_UNKNOWN |
| Seed2.0 Mini | 批量台账、标记、低风险整理 | SEED_OFFICIAL | RUNTIME_UNKNOWN |
| Seed1.8 | Legacy 通用 Agent | SEED_OFFICIAL / LEGACY | RUNTIME_UNKNOWN |
| Seed1.6 | Legacy 多模态/自适应思考 | SEED_OFFICIAL / LEGACY | RUNTIME_UNKNOWN |
| Seed1.5-VL | Legacy 视觉语言分析 | SEED_OFFICIAL / LEGACY | RUNTIME_UNKNOWN |
| Seed1.5 / Doubao-1.5-pro | 旧环境兼容 | SEED_OFFICIAL / LEGACY | RUNTIME_UNKNOWN |

规则：平台未公开实际推理模型时记录 `reasoning_model: UNKNOWN / selection_source: PLATFORM_DEFAULT`，不得猜型号。

## 3. 图片生成 / 编辑模型

| 模型/服务 | 项目角色 | 当前已知规格/特点 | 证据 | 小云雀状态 |
|---|---|---|---|---|
| Seedream 5.0 Pro | 人物标准资产、正式 Look、高写实婚纱、重点 Keyframe、精确编辑 | 当前官方原生档 1K/2K；支持交互式编辑 | SEED_OFFICIAL / BYTEPLUS_OFFICIAL | USER_VERIFIED_RUNTIME（平台曾出现）；AGENT_DIRECT_CALLABLE UNKNOWN |
| Seedream 5.0 Lite | 方案探索、复杂理解、场景与布局、低成本候选 | 当前官方原生档 2K/3K/4K | BYTEPLUS_OFFICIAL | RUNTIME_UNKNOWN |
| Seedream 4.5 | 强身份保持、多图主体锁定、严格参考编辑 | 当前官方原生档 2K/4K | SEED_OFFICIAL / BYTEPLUS_OFFICIAL | RUNTIME_UNKNOWN |
| Seedream 4.0 | 通用生成/编辑、场景 | 当前官方原生档 1K/2K/4K | BYTEPLUS_OFFICIAL | RUNTIME_UNKNOWN |
| SeedEdit 3.0 | 保守局部编辑、目标区域维修 | 任务型编辑候选 | SEED_OFFICIAL / PROJECT_RECORD | RUNTIME_UNKNOWN |
| Anycook 影视版 | 小云雀图片候选 | 技术底层/规格未公开确认 | USER_VERIFIED_RUNTIME | UI/USER observed；AGENT_DIRECT_CALLABLE UNKNOWN |
| Anycook 标准版 | 小云雀图片候选 | 技术底层/规格未公开确认 | USER_VERIFIED_RUNTIME | UI/USER observed；AGENT_DIRECT_CALLABLE UNKNOWN |
| Anycook 创意版 | 小云雀图片候选 | 技术底层/规格未公开确认 | USER_VERIFIED_RUNTIME | UI/USER observed；AGENT_DIRECT_CALLABLE UNKNOWN |
| 旗舰生图 V2-Pro | 场景/编辑候选 | 底层模型、参考上限、原生尺寸均不得猜测 | USER_VERIFIED_RUNTIME / PROJECT_RECORD | UI/USER observed；AGENT_DIRECT_CALLABLE UNKNOWN |
| 即梦AI 图片生成 4.6 | 企业/专项图片候选 | ByteDance 关联图片服务 | BYTEPLUS_OFFICIAL / XYQ_SERVICE | RUNTIME_UNKNOWN |
| 即梦文生图 3.1 | 企业文生图候选 | ByteDance 关联服务 | BYTEPLUS_OFFICIAL | RUNTIME_UNKNOWN |
| 即梦文生图 3.0 | 企业文生图候选 | ByteDance 关联服务 | BYTEPLUS_OFFICIAL | RUNTIME_UNKNOWN |
| 即梦图生图 3.0 智能参考 | 参考式图像编辑/生成候选 | 文本编辑并保持人物/细节能力 | BYTEPLUS_OFFICIAL | RUNTIME_UNKNOWN |

### 图片模型治理

- 模型分辨率、参考上限、价格、并发、地区、生命周期都属于 `MODEL_SPEC_IS_VERSIONED_EVIDENCE`，必须带 `verified_at / source / model_version / platform`。
- 任何“最高版本”都不自动成为所有任务默认模型；身份稳定、编辑性、质量、成本与任务适配共同决定路由。
- 用户实测 UI 模型必须保留真实名称，不得擅自把 Anycook、旗舰生图 V2-Pro 映射成某个 Seedream。

## 4. 视频模型

| 模型 | 项目角色 | 当前已知能力定位 | 证据 | 小云雀状态 |
|---|---|---|---|---|
| Seedance 2.5 | 正式 VIDEO_SHOT / VIDEO_SEQUENCE / VIDEO_EDIT 主力候选 | 官方最长单次约30s；多模态参考；延长；定向编辑；专业运镜/表演 | SEED_OFFICIAL / XYQ_DIRECT | 平台存在；具体 Skill 调用需 Runtime Preflight |
| Seedance 2.0 | 多模态参考、特定任务、2.5 备用 | 文/图/视频/音频联合参考；多镜头音视频 | SEED_OFFICIAL | RUNTIME_UNKNOWN |
| Seedance 2.0 Mini | 低成本/轻量候选 | BytePlus 2.x 服务目录存在 | BYTEPLUS_OFFICIAL | RUNTIME_UNKNOWN |
| Seedance 2.0 Fast / fast 720p | Previz、动作/构图/节奏测试 | 快速低成本路线 | BYTEPLUS_OFFICIAL / PROJECT_RECORD | RUNTIME_UNKNOWN |
| Seedance 1.5 Pro | 对白/音画/兼容任务候选 | Legacy 专项 | SEED_OFFICIAL / PROJECT_RECORD | RUNTIME_UNKNOWN |
| Seedance 1.0 | Legacy 兼容 | 旧视频生成路线 | SEED_OFFICIAL / LEGACY | RUNTIME_UNKNOWN |

规则：`30s capability != 30s design default`。VF01/VF02/VF03 按导演控制、人物稳定、物理复杂度与剪辑需求决定 Shot/Sequence 长度。

## 5. 视频专项服务

以下是独立专项能力，不强行归入 Seedance 家族：

| 服务 | 推荐角色 | 证据 | 小云雀状态 |
|---|---|---|---|
| 即梦AI 视频生成 3.0 Pro | 专项视频候选 | PROJECT_RECORD / XYQ_SERVICE | RUNTIME_UNKNOWN |
| 即梦AI 视频 3.0 1080P / 720P | 专项视频候选 | PROJECT_RECORD / XYQ_SERVICE | RUNTIME_UNKNOWN |
| 动作模仿 2.0 | 行走、转身、舞蹈、裙摆等动作参考/迁移 | PROJECT_RECORD / XYQ_SERVICE | RUNTIME_UNKNOWN |
| OmniHuman 1.5 | 数字人口播、邀请片、特殊角色表演 | PROJECT_RECORD / BYTEPLUS_OFFICIAL | RUNTIME_UNKNOWN |
| OmniHuman 1.0 快速模式 | 低成本/快速人物视频候选 | PROJECT_RECORD | RUNTIME_UNKNOWN |
| 视频翻译 2.0 | 国际婚礼、多语言派生 | PROJECT_RECORD / XYQ_SERVICE | RUNTIME_UNKNOWN |
| 字幕擦除 | 后期视频清理 | PROJECT_RECORD / XYQ_SERVICE | RUNTIME_UNKNOWN |

## 6. 音频 / 音乐 / 语音模型

| 模型/服务 | 推荐角色 | 证据 | 小云雀状态 |
|---|---|---|---|
| Seed Audio 1.0 | Speech + SFX + Ambience 场景声音、后期声音候选 | SEED_OFFICIAL | RUNTIME_UNKNOWN |
| Seed-Music | Picture Lock 后音乐候选 | SEED_OFFICIAL / PROJECT_RECORD | RUNTIME_UNKNOWN |
| SeedRealtime | 实时语音/音频候选 | SEED_OFFICIAL / PROJECT_RECORD | RUNTIME_UNKNOWN |
| Seeduplex | 双向语音/对话候选 | SEED_OFFICIAL / PROJECT_RECORD | RUNTIME_UNKNOWN |
| Seed LiveInterpret 2.0 | 实时翻译/国际婚礼候选 | SEED_OFFICIAL / PROJECT_RECORD | RUNTIME_UNKNOWN |
| Seed Realtime Voice | 实时语音候选 | SEED_OFFICIAL / PROJECT_RECORD | RUNTIME_UNKNOWN |

Seed Audio 1.0 的官方对白时间控制可达到约 100ms；这只说明模型能力，不等于当前小云雀 Skill 已可直接调用。

影视硬规则仍是：Shot Production 前后只保留同期声；非剧情 BGM 和默认 VO 不进入 Shot Generation；背景音乐在 Picture Lock 后加入。

## 7. 3D / 空间预演模型与工具

| 模型/工具 | 推荐角色 | 证据 | 小云雀状态 |
|---|---|---|---|
| Seed3D 2.0 | Scene Blockout、布局、可模拟 3D 资产、空间规划 | SEED_OFFICIAL | RUNTIME_UNKNOWN |
| Seed3D 1.0 | Legacy 3D 候选 | SEED_OFFICIAL / LEGACY | RUNTIME_UNKNOWN |
| 小云雀 3D导演台 | Blocking、Camera Station、Camera Path、空间预演 | XYQ_DIRECT / USER_OBSERVED | UI_AVAILABLE；AGENT_DIRECT_CALLABLE UNKNOWN |
| 小云雀多轨编辑器 | 视频剪辑/多轨后期候选 | XYQ_DIRECT / USER_OBSERVED | UI_AVAILABLE；AGENT_DIRECT_CALLABLE UNKNOWN |

不得根据 UI 名称编造 3D 坐标、骨骼、路径或 API 字段。

## 8. 任务角色路由

统一抽象角色：

`REASONING_MODEL / IMAGE_IDENTITY_MODEL / IMAGE_CREATIVE_MODEL / IMAGE_EDIT_MODEL / IMAGE_SCENE_MODEL / IMAGE_KEYFRAME_MODEL / VIDEO_SHOT_MODEL / VIDEO_SEQUENCE_MODEL / VIDEO_EDIT_MODEL / AUDIO_POST_MODEL / PREVIS_3D_TOOL`

每个项目建立 `MODEL_PLAN`，至少记录：

`task_role / selected_model / model_version_if_visible / evidence_status / runtime_status / why_selected / references / prompt_version / fallback / switch_reason`

用户不需要每个 Shot 重新选模型；只在模型不可用、质量/成本/隐私/能力变化、A/B 证据显示需要切换或用户要求时重新确认。

## 9. Runtime Preflight

至少在以下节点重新扫描真实能力：

1. 第一次人物正式生图前；
2. 第一次 Look/Scene 编辑前；
3. 婚纱影视分支启动前；
4. 第一次视频编辑/延长/音频后期前；
5. 已选模型失败、下线、限额或能力变化时。

任何无法确认的字段记录 `UNKNOWN`，不使用旧聊天记忆冒充实时平台事实。
