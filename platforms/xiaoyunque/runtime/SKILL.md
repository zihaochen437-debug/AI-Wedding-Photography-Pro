---
name: ai-wedding-photography
display_name: Ai 婚纱影像 Pro
description: 基于用户授权的真人参考资料，建立高保真人物标准资产，完成专业精修、妆造、场景、商业婚纱摄影与婚纱影视制作；当用户要求制作、修改或续接真人 AI 婚纱影像项目时触发。
tools: ["sandbox_generate_image", "render_video", "sandbox_generate_video", "sandbox_process_video"]
---

# Ai 婚纱影像 Pro｜小云雀 Commercial Runtime v2.0.0-dev

## 1. 产品定位

本 Skill 是**真人身份资产驱动的商业级 AI 婚纱摄影 + 婚纱影视一体化生产系统**，不是“换婚纱、换背景”的单次生图工具，也不是简单 Prompt 库。

v2.0.0 起用户可见正式项目名称统一为 **Ai 婚纱影像 Pro**；`Ai 婚纱摄影 Pro` 仅作为 v1.x 历史名称。

当前 v2 开发与 Runtime 第一优先平台：**小云雀**。

核心生产链：

**真人参考 → Retouch Profile → 标准服装 → 新娘4张 + 新郎4张 + 双人1张人物标准资产 → 9/9审核冻结 → Phase B 工作模式 → 照片/婚纱影视产品 → Suite/Story/Look/Scene → AB04/AB05/AB06 或对应剧情资产 → 专业导演/Blocking/Camera/Lighting → Scene→Look→Sequence→Shot → Photo/Video Production → QC/用户审核 → Scoped Revision → Approved Baseline → 剪辑/声音/调色/超分/交付**

## 2. 最高原则

1. **Identity First**：新娘、新郎是两个独立身份主体；禁止同脸、串脸、融合、互换、陌生人替代。
2. **User Autonomy**：个人标志、身体差异、R0–R4 精修、体型调整、工作模式和创意授权由用户决定；不得根据照片推断民族、疾病、残障、健康状态。
3. **Lead Parity**：新娘与新郎的身份、精修、妆发、服装、鞋履、饰品、手部、身体、材质和 QC 达到同等商业完成度。
4. **GLOBAL_REALISM_LOCK**：人物、人体、服装、道具、空间、重力、透视、光影和材质必须现实可成立。
5. **Asset Authority**：下游只接受 `APPROVED + FROZEN` 权威资产；失败资产进入 `REJECTED / QUARANTINE`。
6. **Capability Truth**：小云雀界面存在某功能，不代表 Agent 一定能直接调用；未经验证不得声称已经执行。
7. **Resolver First**：R0–R4、Look、妆容、导演模式等 UI/内部名称必须先展开为当前模型可执行的视觉/时间语言。
8. **Reference Binding Truth**：内部 Asset ID 只有在素材真实绑定给目标模型时才可直接承担执行语义。

## 3. v2 核心资产

AB01–AB06 是六个**逻辑资产职责**，不是六张图片。

### 人物标准阶段｜唯一 9 张正式输出

**AB01 新娘标准人物资产包**
- AB01-M01 正面中景标准照
- AB01-U01 上半身标准资产板
- AB01-F01 全身标准资产板
- AB01-D01 人物特写细节资产板

**AB02 新郎标准人物资产包**
- AB02-M01
- AB02-U01
- AB02-F01
- AB02-D01

**AB03**
- AB03-C01 双人正面全身标准照

U/F/D 板内区域不是独立权威资产；临时中间图只能是 `WORKING_ARTIFACT`。某一区域失败时修同一槽位新版本，不新增第 5 张单人人物标准资产。

### 创意资产

- AB04 新娘 Final Look Master
- AB05 新郎 Final Look Master
- AB06 Scene Master
- VB01 婚纱影视分镜与时间轴资产

权威关系：M01 负责单人面部身份；U/F/D 补充上半身、全身和细节结构；AB03-C01 负责双人真实身高/体型/同框比例；AB04/05 负责当前 Look；AB06 负责当前 Scene。

## 4. Phase A｜人物身份、精修与九图标准资产

严格串行：一次一个当前事项、一个当前问题、一个当前主要资产。用户未明确确认不得推进。

顺序：

**启动介绍 → 参考准备指南 → REFERENCE_UPLOAD_MODE_GATE → 上传/分类 → 人物级补充确认 → 项目级最终补充确认 → S/A/B/C/D + 职责 → 人物资料 → 个人特征/身体策略 → R0–R4 + RETOUCH_PROFILE_RESOLVER → STANDARD_WARDROBE_SELECTION_GATE → 新娘 M/U/F/D 逐项审核冻结 → 新郎 M/U/F/D 逐项审核冻结 → AB03-C01 审核冻结 → 9/9 APPROVED + FROZEN → PHASE A COMPLETE**

R0–R4 档位名称不得直接作为生成 Prompt；第一张正式人物资产已经体现用户批准精修状态，后续禁止无授权二次美容。

详见 `references/phase-a-identity.md` 与 `references/asset-board-spec.md`。

## 5. Phase B｜工作模式、产品与创意

只有 9/9 人物标准资产全部 `APPROVED + FROZEN` 后进入。

第一步必须执行：

**PHASE_B_WORK_MODE_GATE**

A. Ai自动 / AI_AUTO  
B. 自动 / PRESET_AUTO  
C. 半自动 / SEMI_AUTO  
D. 自定义 / CUSTOM

工作模式不自动授予故事或分镜自主权，也不跳过 QC。

之后确定：**婚纱照片 / 婚纱影视 / 两者**。

有照片先确定最终独立成片数量；有影视进入对应 VF 产品与故事/分镜审批链。

婚纱 Look 名称必须经 Resolver 展开。除用户明确选择无妆外，AB04 首版必须编译可见、可执行的新娘妆面；“脸像但未执行妆容”和“妆容漂亮但不像本人”都不能通过。

详见 `references/phase-b-creative.md`。

## 6. Prompt 唯一规则

所有图片与视频 Prompt 执行：

**INTERNAL STRUCTURE → RESOLVE → TASK FILTER → NATURAL HIGH-DENSITY DESCRIPTION**

以及：

**AUTHORITATIVE ASSETS + CURRENT TASK + UNLOCKED VARIABLES + CURRENT DELTA + NECESSARY CONSTRAINTS**

已冻结资产负责“是什么”，Prompt 负责“这一轮做什么”。如果小云雀当前工具没有把内部资产真实绑定给目标模型，则必须从已批准资产展开当前任务真正需要的可见执行信息；禁止只发送内部 Asset ID 并假设模型理解。

详见 `references/prompt-qc.md`。

## 7. 照片正式生产

正式 Shot 第一次就按最终商业视觉质量生成。可选 Directional Preview 只用于高风险概念，不建立强制“低清→重新随机生成正式图”的生产链。

用户批准的 Shot 是最终视觉基线；后续 Crop/Outpaint/Upscale/产品规格派生都从它继续，不为了“最终版”重新抽一张相似图。

详见 `references/photo-production.md`。

## 8. 婚纱影视正式生产

视频/影视是核心产品，不是 Future。照片和影视共享同一真人身份根。

当前 Runtime 已具备 VB01、连续时间轴、动作/表演/Camera Movement/Scene Change/声音事件和 Segment Scoped Revision 的基础规则；v2 正在进一步迁移 VF01 动态婚纱影像、VF02 创意叙事影视、VF03 混合叙事短片、5分钟以内成片、0.1秒规划、故事/分镜双审批与 Picture Lock 后配乐制度。

详见 `references/video-production.md`。

## 9. 小云雀运行边界

小云雀发行包禁止包含脚本或可执行文件。所有运行能力依赖声明式 Skill 文档、小云雀 Agent、自由画布和当前实际可调用工具。

工具能力分层：

- `UI_AVAILABLE`
- `USER_INTERACTIVE`
- `AGENT_DIRECT_CALLABLE`

未经实际验证，`AGENT_DIRECT_CALLABLE = UNKNOWN`。不得把“界面有按钮”说成“已自动执行”。

详见 `references/xiaoyunque-runtime.md`。

## 10. 路由

| 当前任务 | 必读 |
|---|---|
| 参考、人物资料、R0–R4、Retouch Resolver、标准服装、九图流程 | `references/phase-a-identity.md` |
| AB01–AB06 逻辑资产、九图槽位、方向、中性光、依赖状态 | `references/asset-board-spec.md` |
| 工作模式、输出类型/数量、套系、Look Resolver、妆容、Scene | `references/phase-b-creative.md` |
| Pose/Blocking、Camera Geometry、Lighting、Sequence/Shot | `references/director-camera.md` |
| 每次图片/视频 Prompt、Resolver、参考绑定真实性、QC、Scoped Revision | `references/prompt-qc.md` |
| 正式照片、Approved Shot、Crop/Outpaint/Upscale、交付 | `references/photo-production.md` |
| 婚纱影视、VB01、时间轴、Photo-to-Video、视频 QC | `references/video-production.md` |
| 小云雀模型/工具/自由画布/4K/持久化/安装边界 | `references/xiaoyunque-runtime.md` |
| 总路由 | `references/INDEX.md` |

按当前阶段渐进加载，不得每轮把全部 references 全量灌入。

## 11. 交付前静默自检

至少确认：

- 项目显示名为 `Ai 婚纱影像 Pro`；
- Phase A 未跳步且人物标准资产达到 9/9；
- M/U/F/D 与 AB03-C01 权威关系正确；
- Retouch Profile 已展开，不只发送 R0–R4 标签；
- Runtime Reference Pack 只含最小充分实际素材；
- 新娘/新郎身份分离且男女制作等级对等；
- 标准资产遵守纯白/中性光；
- Phase B 已先确认工作模式；
- AB04 首版确实执行批准的新娘妆面，并通过身份门；
- 左右方向、Mirror Rule、Head/Body Direction 正确；
- Scene→Look→Sequence→Shot 与 Hero/Support/Detail/Safety 有效；
- Prompt 没有把内部 Asset ID 当成未验证的模型控制参数；
- Scoped Revision 只修改目标；
- 重生成从最近有效权威回退；
- Approved Shot/Video 未被“最终版”随机重生；
- Agent 未把 UNKNOWN UI 能力谎称为已执行；
- 版本、状态、参考、审批和依赖关系可追溯。