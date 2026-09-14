# Ai 婚纱影像 Pro

[English](README.md) | [简体中文](README.zh-CN.md)

> **v2.0.0-dev 开发中。** 从 v2.0.0 起，项目正式名称统一为 **Ai 婚纱影像 Pro**。`Ai 婚纱摄影 Pro` 仅作为 v1.x 历史名称保留。

**Ai 婚纱影像 Pro** 是一套以真人身份高保真为核心、面向商业婚纱摄影与婚纱影视制作的 AI 生产系统。它不是固定模板库，也不是“换婚纱/换背景”的单次生成工具。

项目覆盖真人身份资产、精修、妆造、Scene、摄影导演、策划、编剧、剧本拆分、影视导演、表演指导、摄影指导、服化道、分镜、Prompt Compiler、受控修订、剪辑、声音、调色、QC 与商业交付。

## 当前开发范围

### 当前第一优先 Runtime：小云雀

v2.0.0 当前开发、运行验证和商业流程收口只以 **小云雀** 为第一优先平台。

历史豆包等 Adapter 与 v1.x Release 继续保留用于追溯和研究，但不参与当前小云雀 Runtime 的默认决策。

Universal Core 仍保持平台无关：未来增加其他 Adapter 时，可以改变“怎么执行”，但不得静默削弱身份、审批、用户自主、Asset Authority、Scoped Revision、声音边界或 QC。

## v2 核心变化

### 1. 人物标准资产：4 + 4 + 1

新娘 4 张正式人物标准输出：

- M01 正面中景标准照
- U01 上半身标准资产板
- F01 全身标准资产板
- D01 人物特写细节资产板

新郎同样 4 张，再增加 1 张 `AB03-C01 双人正面全身标准照`，人物标准阶段共 **9 张正式输出**。

AB01/AB02 是逻辑资产包；AB03 是唯一双人比例母版。板内多视角区域不是新的权威人物资产。

### 2. 精修在第一张人物资产前确定

R0–R4 只作为用户选择入口，必须由 `RETOUCH_PROFILE_RESOLVER` 展开为皮肤、五官边界、头发/胡须、牙齿、肩颈、手部、身体姿态和个人标志等具体生产要求。

第一张正式人物资产已经体现用户批准的精修状态；后续不得反复“再美化一次”导致身份漂移。

### 3. Phase B 先选择工作模式

进入婚纱创意与产品设计前，先选择：

- Ai自动 `AI_AUTO`
- 自动 `PRESET_AUTO`
- 半自动 `SEMI_AUTO`
- 自定义 `CUSTOM`

工作模式只改变默认决策权与交互密度，不自动授予故事或分镜自主权，也不跳过 QC。

### 4. Look 与妆容必须显式执行

风格名称不是生成 Prompt。新娘 AB04 首版除非用户明确选择无妆，否则必须展开真实可见的底妆、眉、眼影、眼线、睫毛、腮红、修容、高光、唇妆、妆容强度和皮肤纹理要求，并同时通过人物身份门。

### 5. 专业摄影导演

照片生产采用 `DIR01 → Shot List → Coverage Preflight → Shot`。

导演系统区分 Story Direction、Performance Direction、Physical/Cinematography Direction 和 Model Prompt Compiler。Pose、表情、视线、手部、道具、Blocking、Camera、Lighting、Physics 和 Shot Diversity 均作为专业生产变量管理。

### 6. 三类婚纱影视

- **VF01 动态婚纱影像**：把 Approved Wedding Photo 沿时间扩展成动态叙事。
- **VF02 创意叙事婚纱影视**：根据情侣故事或创意重新设计剧情角色状态、服装、道具和 Scene。
- **VF03 混合叙事婚纱短片**：将情侣故事线与婚纱影像线融合成完整叙事。

最终成片最长 **5 分钟以内**。故事设计与正式分镜默认分别由用户确认；只有对应 `STORY_AUTONOMY` / `STORYBOARD_AUTONOMY` 被明确授权时，才跳过相应人工确认。

影视时间线按 **0.1 秒**记录，但模型 Prompt 的实际时间控制粒度必须根据当前视频模型真实能力适配；最终剪辑点吸附实际帧边界。

Picture Lock 前禁止非剧情背景音乐；Shot Production 只保留同期对白/誓言、呼吸、Ambience、Foley、剧情内声源和 Silence，默认 VO 与 BGM 后期加入。

## 核心理念

- **人物身份第一，创意第二。**
- 新娘和新郎是两个独立身份，禁止串脸、同脸、融合和身份互换。
- 已经审核冻结的资产就是语义权威。
- Prompt 执行 `Authoritative Assets + Current Task + Unlocked Variables + Delta + Necessary Constraints`。
- 内部 Asset ID 只有在素材真实绑定给模型时才可直接承担执行语义，否则必须展开当前任务所需的已批准信息。
- 预设故事、风格、服装、妆容、场景、道具、动作、镜头等都只是商业起点，**包括但不限于**。
- 修改必须受控：只修改目标，保留其他已批准决定。
- Approved Shot / Video 是最终视觉基线，不为了“最终版”重新随机生成。
- 小云雀 UI 能力、用户可操作能力和 Agent 可调用能力不能互相推导。

## 模型治理

项目保留完整模型/专项服务 Catalog，同时 Runtime 动态发现实际可用能力。

候选范围包括 Seed2.x 推理模型、Seedream/SeedEdit、Anycook、旗舰生图 V2-Pro、Seedance 2.5/2.0/Legacy、即梦专项视频、动作模仿、OmniHuman、Seed Audio/Seed-Music/语音系列、Seed3D 与小云雀 3D导演台/多轨编辑器。

**Catalog 收录不等于当前小云雀账号可调用。**关键阶段必须 Runtime Preflight；商业默认路由必须经过受控 A/B 测试，而不是按版本号猜“最高模型”。

## 架构

```text
Source Archive / Research
        ↓
Evidence / Skill Ingestion
        ↓
Active Canon
        ↓
Universal Core
        ↓
Xiaoyunque Adapter
        ↓
Compact Runtime
        ↓
Runtime Preflight + Project State
        ↓
Photo / Film Production
```

仓库主要结构：

```text
core/                 平台无关的当前有效生产规则与契约
platforms/xiaoyunque/ 当前第一优先小云雀 Adapter / Runtime
platforms/doubao/     历史 Adapter，供 v1.x 追溯与研究
docs/                 架构、流程、Prompt 与研究文档
tools/                开发/历史确定性工具；不进入小云雀正式 Runtime
examples/             仅使用可公开的安全示例
tests/                Canon、Core 与 Runtime 回归验证
.github/               Issue、PR 与协作工作流
```

详细说明见 [架构总览](docs/architecture/overview.zh-CN.md)。

## 生产能力范围

包括但不限于：

- 真人参考资料接收、评级、职责分配和最小充分参考包；
- R0–R4 用户自主精修与 Resolver；
- 9 张人物标准资产、AB04/05 Look、AB06 Scene；
- 新娘/新郎完整妆造、服装、饰品、道具和宠物身份；
- Scene → Look → Sequence → Shot 商业摄影组织；
- DIR01、Hero / Support / Detail / Safety Shot；
- Performance / Blocking / Camera Geometry / Lighting / Motion Physics；
- AI 原生正式照片、Scoped Revision 与 Approved Baseline；
- VF01/VF02/VF03 婚纱影视；
- VP01 / VS01 / VD01 / VC01 / VB01 / VSL01 / VA01 / EDL01；
- Take、Continuity、视频局部修订、剪辑、声音、音乐、调色、VFX/Cleanup 和 Master；
- 完整模型 Catalog、Runtime Preflight、Model Plan 与受控模型 A/B 测试。

## 参与贡献

欢迎摄影师、婚纱造型师、影视策划、编剧、导演、摄影指导、灯光师、表演指导、美术/服化道、剪辑/声音/调色从业者，以及 AI/Agent 工程师参与。

提交 PR 前请阅读 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md)。

适合贡献的方向包括：

- 小云雀真实模型/工具能力验证；
- 人物一致性、妆造、编辑越界、视频连续性等回归案例；
- 摄影、影视导演、灯光、表演、Script Breakdown、剪辑和声音知识；
- Seedance / Seedream 等当前模型的受控生产测试；
- 安全的合成人物或明确授权素材示例；
- 中英双语文档和行业资料来源核验。

## 隐私与数据安全

**禁止向公开仓库提交真实客户照片、私人参考资产、健康/身体敏感资料、授权记录、API Key、Token 或私人项目状态。**

示例和测试使用合成人物、明确许可公开的素材，或拥有公开授权的内容。

详见 [SECURITY.md](SECURITY.md)。

## 项目状态

- 最新稳定公开 Release：**v1.9.0**（历史基线）
- `main`：**v2.0.0-dev / Ai 婚纱影像 Pro** 开发中
- 当前第一优先 Runtime：**小云雀**
- 当前阶段：上游人物/精修/妆造、导演、VF01/VF02/VF03、模型治理与验证体系迁移到 v2；尚未发布 v2.0.0 正式 Release。

## License / 许可证

本项目采用 **Apache License 2.0**。详见 [LICENSE](LICENSE) 与 [NOTICE](NOTICE)。

除非明确另行标注，贡献者主动提交并合并到本仓库的贡献按同一 Apache-2.0 条款提供。