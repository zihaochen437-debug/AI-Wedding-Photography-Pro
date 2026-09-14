# Phase A｜人物身份、参考资料与精修

> v2.0.0 开发规则。Phase A 必须严格单项串行：一次只处理一个当前核心问题或资产，用户未明确确认不得进入下一项。

## 1. 参考照片准备指南

先说明：参考资料质量决定人物高保真上限；资料不足可以继续，但必须明确风险。无真人参考进入 `AI_CREATIVE`，不得宣称真人高保真还原。

真人高保真最低：新娘、新郎各至少 1 张清晰正面标准人像。

商业推荐每人：正面半身、鼻尖朝画面左侧约45°、鼻尖朝画面右侧约45°、左完整侧面、右完整侧面、背面半身；双人再提供同一地面、同一前后平面的并排直立全身照。

## 2. REFERENCE_UPLOAD_MODE_GATE

A. 新娘、新郎、双人混合上传  
B. 单人分批上传  
C. 先新郎，再新娘  
D. 先新娘，再新郎  
E. 自定义顺序

混合上传后整理：`BRIDE_REFERENCES / GROOM_REFERENCES / COUPLE_REFERENCES / UNRESOLVED_REFERENCES`。归属不清必须询问，不得猜。

## 3. 两级补充确认

### 人物级
每完成一人的资料接收后询问是否还补：正面、左45、右45、左侧面、右侧面、背面、全身、手部、个人特征、其他。

### 项目级
正式资产制作前再次询问：补新娘、补新郎、补双人并排全身、补身高/体型/年龄、补个人特征、补身体结构/辅助器具、其他。只有用户明确“没有，按当前资料继续”才关闭 Reference Intake。

## 4. 参考评级与职责

每张参考同时记录 S/A/B/C/D 和职责：正面身份 / 左45 / 右45 / 左侧面 / 右侧面 / 全身 / 双人比例 / 个人特征 / 辅助 / 排除。

不同照片不能平权平均。正式生成使用 `MINIMUM_SUFFICIENT_REFERENCE_PACK`。

原图已足够标准时优先做裁切、背景统一、曝光、白平衡、清晰度和必要自然处理，不为了“统一”重新造一个 AI 人物；缺失角度才允许 AI 推演，且推演结果不得反写成用户真实证据。

## 5. 人物基础资料与敏感边界

逐项确认：单人/双人、年龄或年龄段、身高、双人身高差、体型及用户愿意提供的其他信息。

民族、疾病、健康、残障和真实身体差异完全自愿，不得根据照片推断。

不可见区域使用：`REFERENCE_CROPPED / REFERENCE_OCCLUDED / ANGLE_NOT_VISIBLE / BODY_STRUCTURE_UNCERTAIN`。“没拍到”不能解释为“身体不存在”。

## 6. PERSONAL_SIGNATURE_PROFILE

个人特征由用户决定：长期保留 / 仅标准资产保留 / 随套系调整 / 移除 / 自定义。

可包括眼镜、美瞳、耳饰、项链、戒指、手表、痣、雀斑、疤痕、纹身、胡须、牙齿、发际线、假肢、轮椅、拐杖等用户主动提供的信息。

AI 创作性身体补全必须建立独立创作分支、单独审批，不反写为真实人物标准。

## 7. RETOUCH_BEFORE_STANDARD_ASSET

R0–R4 必须在第一张正式人物资产生成前确定；UI 档位名称不得直接作为模型 Prompt。

- **R0 原貌级**：只做曝光、白平衡、背景、清晰度与明显技术瑕疵的标准化，不主动年轻化、瘦脸、磨平皮肤或移除个人标志。
- **R1 自然级**：轻度整理暂时性皮肤问题、油光、飞发和牙面色差；保留毛孔、年龄感、脸型和个人标志。
- **R2 商业自然级**：默认推荐。均匀但不塑料化的肤色与皮肤整理，适度减轻暂时性黑眼圈/泛红/油光，整理眉毛、发丝、胡须、牙齿与肩颈姿态；保持真实骨相、五官比例、年龄、体量与可识别特征。
- **R3 商业强化级**：在 R2 基础上允许更明显的商业级皮肤、轮廓光影、发丝、牙齿、手部和体态整理；除非用户明确授权，不改变脸型、眼鼻唇结构、真实身高或体型类别。
- **R4 用户定制级**：逐项按用户明确要求执行，并继续受身份不变量和真实结构约束。

### RETOUCH_PROFILE_RESOLVER

解析域：

`skin / face_geometry / eyes / brows / nose / lips_teeth / hair_beard / neck_shoulders / hands / body_posture / body_contour / personal_signatures / forbidden_changes`

编译链：

`USER UI → RETOUCH PROFILE ID → PROFILE RESOLVER → USER OVERRIDES → PERSONAL SIGNATURE POLICY → IDENTITY INVARIANT → TASK FILTER → NATURAL LANGUAGE COMPILER`

硬规则：

- `RETOUCH_UI_LABEL_IS_NOT_PROMPT`：不得只发送“R2 商业自然级”等档位名称。
- `STANDARD_ASSET_ALREADY_RETOUCHED`：第一张正式标准资产已经是用户批准的精修状态，不再生成另一套“精修标准照”。
- 后续 U/F/D、双人标准照和 AB04/AB05 继承同一精修基线，禁止无授权二次美容导致 `RETOUCH_DRIFT`。
- 精修与婚礼妆容分离；妆面在 Phase B 的 Look Resolver 中单独编译。

## 8. STANDARD_WARDROBE_SELECTION_GATE

首张正式标准资产前选择一套简洁、自然、无明显 Logo/复杂花纹的男女协调标准服装，并贯穿双方四张单人标准资产与双人正面全身标准照。

商业预设仅供选择，不限制自定义：CW-01 黑白经典；CW-02 奶油白/深海军蓝；CW-03 暖白/深棕；CW-04 浅蓝/深蓝；CW-05 黑/象牙白；CW-06 用户自定义/保留原服装。不得默认灰色标准服装。

## 9. STANDARD_IDENTITY_4_PLUS_1_POLICY

每位人物只有四个正式人物标准输出槽位：

1. `FRONT_MEDIUM_MASTER`｜正面中景标准照
2. `UPPER_BODY_STANDARD_BOARD`｜上半身标准资产板
3. `FULL_BODY_STANDARD_BOARD`｜全身标准资产板
4. `DETAIL_STANDARD_BOARD`｜人物特写细节资产板

双人只增加：`COUPLE_FRONT_FULL_BODY_MASTER`｜双人正面全身标准照。

双人项目人物标准阶段唯一有效的物理输出数量：`4 + 4 + 1 = 9 images`。

多视角只存在于 U/F/D 资产板内部，不再把左45、右45、左右侧面、背面分别注册成新的正式人物资产。板内区域失败时冻结正确区域，仅修失败区域并升级同一槽位版本；不得新增第 5 张单人人物标准资产。

## 10. Phase A 顺序

`启动介绍 → 参考指南 → REFERENCE_UPLOAD_MODE_GATE → 上传/分类 → 人物级补充 → 项目级最终补充 → S/A/B/C/D + 职责 → 人物资料 → 个人特征/身体策略 → R0–R4 + Retouch Resolver → 标准服装 → 新娘 M/U/F/D 逐项审核冻结 → 新郎 M/U/F/D 逐项审核冻结 → 双人正面全身标准照审核冻结 → 9/9 APPROVED + FROZEN → PHASE A COMPLETE`

未达到 `9/9 APPROVED + FROZEN` 时不得结束人物标准阶段。