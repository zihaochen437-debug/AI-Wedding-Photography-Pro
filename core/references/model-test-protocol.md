# Ai 婚纱影像 Pro v2｜模型商业验证协议

模型进入正式商业默认路由前，不能只凭官方宣传、版本号或单张好图。必须在当前平台/账号做受控测试。

## 1. 证据层

测试记录区分：

- `OFFICIAL_CAPABILITY`：厂商能力声明
- `RUNTIME_VISIBLE`：当前小云雀真实可见
- `RUNTIME_CALLABLE`：当前 Agent/工具真实调用成功
- `CONTROLLED_AB_TEST`：同任务受控比较
- `PROJECT_OBSERVATION`：真实项目观察，样本量不足时不泛化

## 2. 测试样本原则

每个模型角色至少准备固定基准任务，保持人物、参考、任务目标和主要 Prompt 意图一致，只改变模型/必要平台参数。

禁止用不同人物、不同构图、不同美化要求得出“模型 A 比模型 B 更好”的结论。

## 3. IMAGE_IDENTITY_MODEL 测试

至少覆盖：

1. 正面中景 M01；
2. U01 多视角上半身板；
3. F01 多视角全身板；
4. D01 眼/鼻/唇/耳/手等细节；
5. AB03-C01 双人正面全身；
6. 男女同时存在时的身份分离；
7. 不对称个人特征与左右方向；
8. 用户选择 R0/R2/R3 后身份保持。

评分至少分开：

`IDENTITY_FIDELITY / MULTI_SUBJECT_SEPARATION / BODY_PROPORTION / HANDS / RETOUCH_COMPLIANCE / REFERENCE_COMPLIANCE / EDITABILITY / AI_ARTIFACTS`

## 4. LOOK / CREATIVE IMAGE 测试

至少覆盖：

- 新娘明确妆面是否真正出现；
- 妆容强度与身份是否同时正确；
- 发型、头纱、饰品、婚纱结构；
- 新郎服装与 Grooming；
- 中式/年代服装和 Scene 的文化一致性；
- 宠物、多道具、多主体；
- 空场景 → 人物合成；
- 真实光学景深和焦平面。

禁止用“更漂亮”替代 Look 执行准确度。

## 5. IMAGE_EDIT_MODEL 测试

固定 Approved Baseline，逐项测试：

- 只改眼妆；
- 只修一只手；
- 只改婚纱局部结构；
- 只修头纱；
- 只改 Scene 一个道具；
- 只做局部纹理恢复。

记录：`TARGET_SUCCESS / IDENTITY_DRIFT / NON_TARGET_CHANGE / COLOR_DRIFT / CAMERA_DRIFT / REFERENCE_DRIFT`。

商业编辑模型的核心不是“会改”，而是“改目标且不破坏其他批准内容”。

## 6. VIDEO_SHOT_MODEL 测试

至少覆盖：

- 单人近景微表演；
- 双人对视/Listening/Reaction；
- 行走、牵手、转身；
- 头纱/裙摆/发丝与风；
- 手部接触与道具；
- 宠物互动；
- 固定机位与受控 Push/Track/Arc；
- 起始帧人物占位；
- End State 连续性；
- 同期对白（若适用）；
- 无背景音乐生产。

评分：

`IDENTITY_FRAME_STABILITY / BODY_PHYSICS / HAND_CONTACT / LOOK_CONTINUITY / PROP_CONTINUITY / CAMERA_COMPLIANCE / FIRST_FRAME / END_STATE / SYNC_SOUND / LIP_SYNC / FLICKER_MORPHING`

## 7. VIDEO_SEQUENCE_MODEL 测试

多镜头/连续段落额外检查：

- Scene Geography；
- Screen Direction；
- Eyeline；
- Match on Action；
- 角色左右关系；
- Lighting/Color 连续；
- 服装/道具状态；
- 内部 Cut 是否随机增加；
- 时间窗口是否遵守当前模型实际粒度；
- 结束状态是否能接下一 Shot。

## 8. VIDEO_EDIT_MODEL 测试

在固定视频上分别测试：

- 只改指定 2–4 秒人物面部；
- 只改 Camera 路径；
- 只替换背景；
- 只修道具；
- 延长尾部；
- 保持其他时间段完全不变。

核心指标：`TEMPORAL_SCOPE_COMPLIANCE / IDENTITY_PRESERVATION / MOTION_CONTINUITY / AUDIO_CONTINUITY / UNREQUESTED_REPAINT`。

## 9. AUDIO_POST_MODEL 测试

仅在 Runtime 可调用时执行：

- Dialogue timing；
- Ambience；
- Foley；
- VO；
- Sound Design；
- Picture Lock 后 Music。

生成期 BGM 抑制失败单独记录 `AUDIO_QC_FAIL`，不能因为其他维度不错而忽略。

## 10. A/B 结论等级

- `GOLD`：多个基准任务稳定通过，可成为当前默认商业路由
- `PASS`：适合特定任务，需要规则约束
- `CONDITIONAL`：只在某些画幅/主体/编辑类型有效
- `EXPERIMENTAL`：样本不足，仅方案探索
- `FAIL`：关键商业门持续失败
- `UNKNOWN`：未实测

## 11. 不允许伪统计

没有足够样本时，不输出虚构的百分比成功率。可以记录实际 `n/N` 与具体失败类型。

例如：`双人身份稳定 7/10；其中 2 次新郎漂移、1 次身高比错误`，优于无证据写“稳定率 90%”。

## 12. Promotion Gate

模型成为某角色默认路由前至少满足：

`RUNTIME_CALLABLE + CONTROLLED_AB_TEST + HARD_FAILURE_RATE 可接受 + 关键域无系统性错误 + 回退路线明确`。

模型版本、平台入口或参考机制变化后，旧结论进入 `NEEDS_REVALIDATION`，不得永久沿用。
