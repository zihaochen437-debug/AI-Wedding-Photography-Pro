# Ai 婚纱影像 Pro v2｜小云雀 Runtime 路由索引

本 Runtime 采用“小云雀原生 Compact Skill”思路：薄 `SKILL.md` + 少量高密度 references + 渐进式加载。可以压缩物理文件数量，但不能压缩业务能力。

| 当前任务 | 必读文档 |
|---|---|
| 启动、参考上传、人物资料、S/A/B/C/D、R0–R4、Retouch Resolver、标准服装、9图人物标准资产 | `phase-a-identity.md` |
| AB01–AB06 逻辑职责、M/U/F/D、AB03-C01、方向、中性光、状态、依赖 | `asset-board-spec.md` |
| Phase B 工作模式、输出类型/数量、Suite/Style、Look Resolver、显式妆容、Scene | `phase-b-creative.md` |
| DIR01、表演、Pose/Blocking、Camera Geometry、Lighting、Physics、商业组片 | `director-camera.md` |
| Resolver、@参考职责、Reference Binding Truth、Asset Authority + Delta、QC、Scoped Revision、重生成 | `prompt-qc.md` |
| 正式照片、Approved Shot、Batch、Crop/Outpaint/Upscale、交付 | `photo-production.md` |
| VF01/VF02/VF03、Story/Storyboard Gate、VB01、0.1s、Take/EDL、无BGM、剪辑声音调色和视频QC | `video-production.md` |
| 思考/生图/编辑/视频/音频/3D模型候选与 Runtime Preflight | `model-catalog.md` |
| 小云雀 Frontmatter/tools、自由画布、能力真实性、持久化 | `xiaoyunque-runtime.md` |

## 全局不可跳过

- v2 用户可见正式名称：`Ai 婚纱影像 Pro`。
- 身份优先、用户自主、男女对等、自然真实写实。
- Phase A 结束条件是人物标准资产 `9/9 APPROVED + FROZEN`。
- AB01/AB02 是四槽人物资产包；AB03 仅为一张双人正面全身比例母版。
- U/F/D 板内区域不是独立正式人物资产；临时中间图只能是 Working Artifact。
- R0–R4、Look、妆容、导演模式等 UI 名称必须先 Resolver 展开。
- Phase B 必须先通过 `PHASE_B_WORK_MODE_GATE`，工作模式不自动取得故事或分镜自主权。
- 除用户明确无妆外，新娘 AB04 首版必须执行已确认妆容并通过身份门。
- 照片正式批量生产前必须有 DIR01 / Shot List / Coverage Preflight。
- VF02/VF03 的故事与 VB01 默认分别需要用户确认；VF01 有明显叙事时同样先确认动态叙事方案。
- 影视最终成片最长 5 分钟；0.1 秒是制作计划/数据精度，模型 Prompt 时间粒度按当前真实能力适配。
- Picture Lock 前禁止非剧情 BGM；正式 Shot 只允许同期/剧情内声音，默认 VO 后期加入。
- 只有 `APPROVED + FROZEN` 可以成为正式下游权威；`REJECTED / QUARANTINE` 不得继续引用。
- 已冻结资产只有在真实绑定给模型时才可用内部 @ID 直接承担执行语义；否则展开当前任务需要的已批准信息。
- 模型 Catalog 是候选目录，不是当前可调用清单；关键阶段必须 Runtime Preflight。
- 小云雀 Runtime 中禁止脚本和可执行文件。
- UI 存在某能力不代表 Agent 可直接调用。
