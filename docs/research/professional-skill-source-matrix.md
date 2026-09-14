# Ai 婚纱影像 Pro｜Professional Skill Source Matrix

> 本文件用于研究来源、许可证、原则提炼与 Canon Promotion 治理。外部 Skill/仓库不是本项目 Runtime 依赖，除非后续另有明确集成决定。

## 1. Ingestion Pipeline

所有外部/用户提供专业 Skill 按以下顺序处理：

`Discover → License Gate → Craft Audit → Extract Principles → Compare Against Canon → Conflict Resolution → Xiaoyunque Translation → Wedding Specialization → Validation → Promote to Canon`

规则：

- 不因为文件名叫“导演 Skill”就直接进入 Canon；
- 不复制第三方长篇文本、模板、示例或模型事实到发行包而忽略许可证；
- 平台/模型事实必须回到官方或当前 Runtime 重新核验；
- 专业方法可以抽象为本项目自己的职责、Schema、Gate、QC 和决策逻辑；
- 与用户明确要求或现有 Active Canon 冲突时必须显式裁定，不能静默覆盖。

## 2. Evidence Types

- `USER_REPO_REFERENCE`：用户 GitHub 中主动提供/收藏的专业仓库
- `USER_PROVIDED_REFERENCE`：用户直接上传到项目的 Skill/资料文件
- `GITHUB_REFERENCE`：外部公开 GitHub 专业项目
- `INDUSTRY_PRACTICE`：成熟影视/摄影生产实践
- `INDUSTRY_STANDARD`：ACES/OCIO/OTIO 等正式标准/行业基础设施
- `OFFICIAL_MODEL_DOC`：ByteDance/BytePlus/小云雀等当前官方模型/平台资料

专业参考优先级不凌驾于官方模型事实、用户当前决策和 Active Canon。

## 3. 用户 GitHub 专业参考池

| Source | Evidence | License | 主要可学习内容 | Adoption |
|---|---|---|---|---|
| `zihaochen437-debug/seedance-2-5-video-director` | USER_REPO_REFERENCE | MIT（已核验） | Asset Lock Table、Seedance 2.5 模式路由、Reference Role、Continuity、Audit | ADAPT / 已吸收 Reference Binding、End State、视频执行原则 |
| `zihaochen437-debug/seedance-2.0` | USER_REPO_REFERENCE | MIT（已核验） | camera/characters/lighting/motion/audio/continuation 等子 Skill 拆分、专业视频 Skill OS | ADAPT / 用于专业职责拆分与模型适配研究 |
| `zihaochen437-debug/visual-skills` | USER_REPO_REFERENCE | CC BY 4.0（已核验，需署名） | Dramaturgy、Director/Screenwriter/Editor 分层、Seedance 2.5 参考、Prompt anti-slop | ADAPT / 原则提炼；不得移除署名要求复制受保护文本 |
| `zihaochen437-debug/XiaoLuo-AI-Drama-Skill` | USER_REPO_REFERENCE | 未在仓库根发现 LICENSE（当前核验） | 剧本分析、编剧、剧本资产 DNA、美术、场景布局、角色服装/动作/表情/道具、拉片 | STUDY / PRINCIPLES ONLY，许可证确认前不复制文本/模板 |
| `zihaochen437-debug/manju-laoli-skill/short-drama-director` | USER_REPO_REFERENCE | MIT（已核验） | Asset-First、Screenplay Gate、Production Ledger、空间顶视图、Dialogue/Emotion/QC、模型适配 | ADAPT / 去掉短剧爽点偏置后用于工业治理 |

## 4. 用户上传导演/表演 Skill

| Source | Evidence | License | 主要原则 | v2 采用方式 |
|---|---|---|---|---|
| `LIRA SKILL.md` | USER_PROVIDED_REFERENCE | 当前资料未明确许可 | Deconstruct/Diagnose/Develop/Deliver、Prompt Signal Density、Minimal Change/Preserve | 原则提炼；形成 Resolver First、Precision > Verbosity、Scoped Revision，不采用其 Higgsfield 固定模型路由 |
| `ACTING SKILL.md` | USER_PROVIDED_REFERENCE | 当前资料未明确许可 | Behavior under pressure、Objective/Obstacle/Tactic/Beat/Subtext、Listening、Eye Life、Business、Proxemics | 原则提炼；形成 Performance Direction；不把“每场必须冲突/失败”等戏剧偏好强制到所有婚纱镜头 |
| `CINEDANCE HIGGSFIELD SKILL.md` | USER_PROVIDED_REFERENCE | 当前资料未明确许可 | Shot Isolation、First Frame、Blocking、Gaze、Camera Side、Optics、Physics、Lighting、Timing、Continuity、Silent QA | 原则提炼；形成 First/End State、Blocking Before Framing、Physics/Lighting Lock；不采用其固定 FOV/英语/外部平台参数为硬规则 |

这些文件作为用户提供的研究材料使用；除非后续许可得到确认，不在公开发行包中复制其原文、长模板或独特示例。

## 5. 用户提供婚纱生产 Prompt Reference Set

研究资料包括：

- 《杜宾也穿高定》
- 《粉彩青花》新中式婚纱
- 《花影新娘》
- 《绛兰》
- 表情控制提示词
- 工笔玉兰提示词

Evidence：`USER_PROVIDED_PRODUCTION_REFERENCE`

已提炼的项目原则：

- `SET_MASTER_LOCK + SHOT_DELTA`
- `REFERENCE_ROLE_SEPARATION`
- `SCENE_FIRST_COMPOSITE_MODE`
- `EXPRESSION_PHYSICALIZATION`
- `POSE_GEOMETRY_LANGUAGE`
- `PHYSICAL_DEPTH_OF_FIELD_RULE`
- `KNOWN_FAILURE_TARGETED_REPAIR`
- `STYLE_SCOPE_BINDING`
- `RISK_AWARE_NEGATIVE_COMPILER`
- 多主体/宠物独立身份与真实尺度

这些资料用于学习商业实战结构，不把具体服装、道具、场景或文案变成项目能力边界。

## 6. 其他已研究 GitHub / Industry References

| Source | 类型 | 用途 |
|---|---|---|
| `0xhughs/director-skills` | GITHUB_REFERENCE / MIT（此前核验） | Story→Screenplay→Shotlist→Visual Bible→Prompt 的子 Skill 路由与 Production Breakdown |
| `DirectorSKILL` | GITHUB_REFERENCE / MIT（此前核验） | Working Director + Previs、Blocking Before Framing、End State、Keyframe Control |
| OpenTimelineIO | INDUSTRY_STANDARD / OSS | VB01/EDL/Timeline 数据模型参考 |
| OpenColorIO / ACES | INDUSTRY_STANDARD | 跨来源素材的 Color Management 思维 |
| Kitsu | INDUSTRY_PRACTICE / OSS | Asset/Shot/Sequence/Edit/Task/Approval/Version 治理 |
| OpenRV | INDUSTRY_PRACTICE / OSS | Frame Review、Compare、Version QC 工作站思维 |
| DreamO / InfiniteYou / Regional Prompting 等 | GITHUB/RESEARCH_REFERENCE | 条件路由、多主体隔离、Identity vs Alignment 等技术设计原则 |

这些项目仅作为架构/专业知识参考，不声明已安装进小云雀 Runtime。

## 7. License Gate

采用状态：

- `STUDY`：只阅读/分析
- `PRINCIPLES_ONLY`：只抽象原则，不复制表达、模板、代码
- `ADAPT_WITH_ATTRIBUTION`：许可证允许改编但需要署名/通知
- `ADAPT`：许可证允许，仍需保持来源记录
- `CANON`：已经经过婚纱化改造、冲突审计、验证并成为本项目规则
- `REJECT`：不采用

许可证未知或不允许商业改编的来源，默认只能 `STUDY / PRINCIPLES_ONLY`。

## 8. Model Facts Gate

第三方 Skill 中关于 Seedance/Seedream/其他模型的时长、分辨率、语法、参考上限、费用等，只能作为搜索线索。

进入 `model-catalog.md` 的当前技术事实需满足至少一种：

- 官方 Seed / BytePlus / 小云雀来源；
- 用户当前 Runtime 实测；
- 明确标记为 `PROJECT_RECORD / RUNTIME_UNKNOWN`。

不得把第三方 Skill 的模型断言直接提升为 `XYQ_DIRECT`。

## 9. Canon Promotion Record

每条从外部来源吸收的规则应能够回答：

```yaml
source:
source_license:
principle:
project_translation:
conflict_checked_against:
xiaoyunque_runtime_assumption:
validation_required:
canon_rule_id:
status:
```

目的是让 Ai 婚纱影像 Pro 最终拥有自己的专业生产体系，而不是多个外部 Skill 的拼接包。
