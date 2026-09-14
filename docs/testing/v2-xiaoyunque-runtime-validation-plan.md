# Ai 婚纱影像 Pro v2｜小云雀 Runtime 与 E2E 验证计划

> 目标：把“平台看得到”“用户能点”“Agent 能调用”“商业结果稳定”四件事分开验证。任何测试都不得上传真实客户私密照片到公开仓库；公开记录只保存去身份化结果、合成身份或结构化结论。

## 1. 测试状态词典

### Capability

- `VERIFIED`：本次当前账号/当前版本真实执行成功
- `OBSERVED`：界面或结果观察到，但未完成完整重复验证
- `UNKNOWN`：没有足够证据
- `UNSUPPORTED`：明确不支持
- `SUPERSEDED`：旧结论已被新测试推翻

### Access Layer

每项能力分别记录：

- `MODEL_AVAILABLE`
- `TOOL_AVAILABLE`
- `UI_AVAILABLE`
- `USER_INTERACTIVE`
- `AGENT_DIRECT_CALLABLE`

禁止用一个字段推导另一个字段。

## 2. 测试环境快照

每次测试先记录：

```yaml
test_session:
  date:
  account_tier_if_visible:
  xiaoyunque_version_if_visible:
  region_if_visible:
  entry_mode:
  free_canvas_available:
  model_selector_visible:
  tools_visible:
  notes:
```

无法看到的字段填 `UNKNOWN`，不猜。

## 3. Model Discovery

### Reasoning

目标：确认是否能看到/选择实际思考模型。

候选 Catalog 包含 Seed2.1 Pro/Turbo、Seed2.0 Pro/Lite/Mini、Legacy Seed 系列；如果小云雀隐藏后台型号，结论必须是：

```yaml
reasoning_model: UNKNOWN
selection_source: PLATFORM_DEFAULT
```

### Image

逐项确认当前是否可见/可选：

- Seedream 5.0 Pro
- Seedream 5.0 Lite
- Seedream 4.5
- Seedream 4.0
- SeedEdit 3.0
- Anycook 影视版
- Anycook 标准版
- Anycook 创意版
- 旗舰生图 V2-Pro
- 即梦相关图片服务（若入口可见）

记录：`visible / selectable / generated_successfully / edit_successfully / actual_output_size / reference_input_behavior`。

### Video

确认：

- Seedance 2.5
- Seedance 2.0
- Seedance 2.0 Mini
- Seedance 2.0 Fast
- Seedance 1.5 Pro / 1.0（若仍存在）
- 即梦视频专项服务
- 动作模仿
- OmniHuman

重点不是型号列表本身，而是实际：生成、参考绑定、延长、编辑、局部重绘、音频、最长可选时长、分辨率和失败提示。

### Audio / 3D

确认 Seed Audio/音乐/语音候选、小云雀音频工具、3D导演台、多轨编辑器的真实入口与 Agent 直接调用状态。

## 4. Tool Callability Tests

每项至少完成“UI观察”和“Agent调用”两个独立测试：

| Capability | UI_AVAILABLE | USER_INTERACTIVE | AGENT_DIRECT_CALLABLE | Evidence |
|---|---|---|---|---|
| Generate Image | | | | |
| Image Edit | | | | |
| Crop/Rotate | | | | |
| Outpaint | | | | |
| Upscale | | | | |
| Local Inpaint | | | | |
| Lighting Adjustment | | | | |
| Camera/View Adjustment | | | | |
| Layer Separation | | | | |
| Makeup/Expression Tool | | | | |
| Generate Video | | | | |
| Video Edit | | | | |
| Video Extend | | | | |
| Video Process/Render | | | | |
| 3D Director Stage | | | | |
| Multitrack Editor | | | | |
| Audio Generation/Edit | | | | |

只有实际工具调用返回结果时才将 `AGENT_DIRECT_CALLABLE` 标为 VERIFIED。

## 5. E2E-01｜人物九图身份链

使用合成/公开许可测试人物 A 与 B。

流程：

`Reference Intake → S/A/B/C/D + roles → R0/R2（至少两档测试） → Standard Wardrobe → Bride M/U/F/D → Groom M/U/F/D → AB03-C01 → 9/9 approval`

必须验证：

- M01 是否本人/同一身份；
- U/F/D 是否真正继承 M01，而不是换人；
- 多视角板是否内部同人；
- 板内局部错误能否只修目标区域；
- 不对称特征和方向是否保持；
- 双人是否不串脸；
- AB03 身高/体型比例是否稳定；
- R2 是否实际执行具体精修，而不是只有名称；
- 标准服装在九图中保持一致。

记录每个槽位：`PASS/FAIL/PARTIAL/NOT_VERIFIED` + failure type。

## 6. E2E-02｜Wedding Look / Makeup

从已冻结九图开始：

1. 选择一个明确 Wedding Look；
2. 编译具体新娘妆面；
3. 生成 AB04；
4. 检查 Identity 与 Makeup Presence；
5. 只修改眼妆一次；
6. 再检查身份漂移；
7. 生成 AB05；
8. 建立临时 Look Review；
9. 建 AB06。

硬检查：

- 首版不是“脸像但没妆”；
- 改妆不改变脸型/年龄；
- 婚纱结构/头纱/饰品不漂；
- 新郎制作等级不低于新娘；
- AB06 Scene 不混入陌生模特。

## 7. E2E-03｜Photo Production

`AB04/05/06 → DIR01 → Shot List → Coverage Preflight → 9或12张正式 Shot`

至少覆盖：

- 环境 Hero；
- 双人全身；
- 半身/近景；
- 单人；
- Detail；
- 一段动作中间态；
- 至少三种视线关系；
- 至少一个有意义道具互动；
- 横竖构图（如果当前套系目标需要）。

测试一次 Scoped Revision，例如只修一只手或只改眼妆，确认其他域不变化。

Shot Diversity 记录真实重复情况，不因为规则存在自动判 PASS。

## 8. E2E-04｜VF01

输入：3–6 张 Approved Wedding Photos。

流程：

`VF01 Brief → Dynamic Narrative Approval → VB01 Approval → Shot/Sequence Generation → Take → Scoped Revision → Assembly/Rough/Fine → Picture Lock → Audio Post/Music → Master`

检查：

- 源照片人物/服装/Scene/构图忠实；
- 动作不是统一眨眼+推镜；
- 头纱/裙摆/头发物理真实；
- 不出现未经要求 BGM；
- End State 能接下一 Shot；
- Picture Lock 后才加 Music。

## 9. E2E-05｜VF02

测试一个 30–60 秒短故事，不要求先做到五分钟。

`Story Concept → User Story Approval → Screenplay → Script Breakdown → Story Looks/Props/Film Scenes → Director/Continuity → VB01 Approval → Shot/Take → Edit/Post`

至少包含：

- 2 个 Scene；
- 2 个 Story Looks 或明确角色状态变化；
- 一个 Prop State 变化；
- 一个 Listening/Reaction Beat；
- 一句现场 Dialogue（如果当前视频模型支持）；
- Story 修改后一次 Stale/Revalidation 测试。

验证纯 VF02 不需要为了流程先生成无用 AB04/05/06。

## 10. E2E-06｜VF03

测试 45–90 秒混合片：

`Story Line Assets + Wedding Line Source → Hybrid Story Approval → Bridge Map → VB01 Approval → Generation → Edit/Post`

至少验证两种 Bridge：

- Match on Action / Motion；
- Audio / Prop / Color / Graphic Match 任选一种。

检查婚纱线是否成为剧情结果而非突然插播，以及 Story/Wedding 两种来源经过 Color/Texture/Sharpness Match 后是否像同一部影片。

## 11. Five-Minute Stress Test

只有短片 E2E 稳定后，再测试 3–5 分钟项目。

重点不追求一次生成，而检查：

- 角色跨 Sequence 连续性；
- Story/Prop/Look 状态长程保持；
- Shot 数量与 Project State 是否可恢复；
- Take/EDL 管理；
- 多 Scene 色彩/声音统一；
- 中断会话后恢复；
- 最终 Master 与平台派生版本。

## 12. Persistence Test

在一个中间 Gate 主动结束会话/项目环境后重新打开：

检查是否能够恢复九图状态、当前工作模式、Look/Scene、DIR01、Story/VB01、Open Revision、Model Plan。

根据结果只允许：`PERSISTED / SESSION_ONLY / UNKNOWN`。

## 13. Regression / Negative Tests

故意测试：

- 用户拒绝 Story；
- Story Autonomy TRUE、Storyboard FALSE；
- Story 修改后旧 VB01 是否继续被错误使用；
- AB04 局部改妆是否导致换脸；
- 模型不可用是否虚构执行成功；
- UI 有超分按钮但 Agent 调用失败；
- 视频生成意外带 BGM；
- Scoped Revision 越界；
- REJECTED 资产是否被继续引用；
- v2 Project State 中断恢复。

## 14. Test Result Record

每个案例记录：

```yaml
case_id:
date:
platform:
model_plan:
input_asset_ids:
prompt_versions:
expected_behavior:
actual_behavior:
qc_evidence_scope:
failures:
revisions:
cost_if_known:
elapsed_steps:
status:
conclusion:
canon_change_required:
```

没有证据的内容写 UNKNOWN，不用“应该可以”填空。

## 15. v2 Release Gate

稳定 v2.0.0 发行前至少需要：

- Source CI PASS；
- E2E-01 九图身份链通过；
- E2E-02 Look/Makeup 通过；
- E2E-03 Photo Production 有完整案例；
- VF01/VF02/VF03 各至少一个短片受控案例；
- Story/Storyboard Gate、No-BGM、Scoped Revision 行为实测；
- Capability Matrix 有当前账号证据；
- Persistence 明确属于 PERSISTED/SESSION_ONLY/UNKNOWN；
- 主要硬失败有明确人工接管路径。

达到这些之前，main 保持 `v2.0.0-dev`，不编译/发布稳定 v2.0.0。
