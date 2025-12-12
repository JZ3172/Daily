"""
USD/moneyGame.py
=================
投资决策概率模型 - 基于二元选择与可能性空间

核心哲学：
- C = 2 (基数: 成功/失败的二元选择)
- N = 10 (周期: 连续决策的时间跨度)
- 可能性空间 = 2^10 = 1024 (样本空间中的所有命运)
  
在1024种可能的投资命运中，只有1条完美路径能实现"指数级回报"。
这个模型量化了在追求高收益时所面临的真实难度空间。

变量说明：
- holder_T: 持有年份 (年数)
- account_T: 账户总额 (最终金额)
- P: 单次成功概率 (0-1之间)
"""

import random
from typing import Dict, List, Tuple
from collections import defaultdict

# =================== 核心参数 ===================
C = 2           # 二元选择基数 (成功/失败)
N = 10          # 决策周期数 (年份)
POSSIBILITY_SPACE = C ** N  # 可能性空间 = 1024

# =================== 模型1: 单次模拟 ===================
def simulate_money_game(
    initial_amount: float,
    years: int,
    success_multiplier: float,
    failure_multiplier: float,
    probability: float
) -> Tuple[float, List[bool]]:
    """
    模拟单一投资命运序列
    
    Args:
        initial_amount: 初始金额
        years: 持有年份 (通常为10)
        success_multiplier: 成功时的增长率 (e.g., 1.1 表示增长10%)
        failure_multiplier: 失败时的衰减率 (e.g., 0.9 表示衰减10%)
        probability: 每年成功的概率 (0-1)
    
    Returns:
        (最终金额, 决策序列)
    """
    amount = initial_amount
    decisions = []  # 记录每一年的决策 (True=成功, False=失败)
    
    for year in range(years):
        if random.random() < probability:
            amount *= success_multiplier
            decisions.append(True)
        else:
            amount *= failure_multiplier
            decisions.append(False)
    
    return amount, decisions


# =================== 模型2: 可能性空间遍历 ===================
def explore_possibility_space(
    initial_amount: float,
    success_multiplier: float = 1.1,
    failure_multiplier: float = 0.9,
    num_simulations: int = 1024
) -> Dict:
    """
    在可能性空间中进行蒙特卡洛模拟
    
    Args:
        initial_amount: 初始金额
        success_multiplier: 成功倍数
        failure_multiplier: 失败倍数
        num_simulations: 模拟次数 (通常为 2^10 = 1024)
    
    Returns:
        统计结果字典
    """
    results = {
        'final_amounts': [],
        'perfect_paths': [],  # 所有成功的路径
        'min_amount': float('inf'),
        'max_amount': 0,
        'avg_amount': 0,
        'median_amount': 0,
        'success_rate': 0  # 正收益的命运比例
    }
    
    positive_count = 0
    
    for _ in range(num_simulations):
        final_amount, decisions = simulate_money_game(
            initial_amount, N, success_multiplier, failure_multiplier, 0.5
        )
        results['final_amounts'].append(final_amount)
        
        # 统计完美路径 (全部成功)
        if all(decisions):
            results['perfect_paths'].append(final_amount)
        
        # 统计正收益命运
        if final_amount > initial_amount:
            positive_count += 1
        
        results['min_amount'] = min(results['min_amount'], final_amount)
        results['max_amount'] = max(results['max_amount'], final_amount)
    
    results['avg_amount'] = sum(results['final_amounts']) / num_simulations
    results['median_amount'] = sorted(results['final_amounts'])[num_simulations // 2]
    results['success_rate'] = positive_count / num_simulations
    
    return results


# =================== 模型3: 单一完美路径 ===================
def calculate_perfect_path(
    initial_amount: float,
    multiplier: float,
    periods: int = N
) -> float:
    """
    计算单一完美路径的结果
    (即：在1024种命运中，那个唯一连续成功的路径)
    
    结果 = initial_amount * (multiplier ^ periods)
    """
    return initial_amount * (multiplier ** periods)


# =================== 输出与分析 ===================
if __name__ == "__main__":
    print("=" * 70)
    print("投资决策概率模型分析")
    print("=" * 70)
    print()
    
    # 基础参数
    initial_amount = 1000.0
    success_multiplier = 1.1   # 成功: 增长10%
    failure_multiplier = 0.9   # 失败: 衰减10%
    
    # ------  模型1: 单次模拟 ------
    print("[模型1] 单一命运序列模拟")
    print("-" * 70)
    final_amount, decisions = simulate_money_game(
        initial_amount, N, success_multiplier, failure_multiplier, 0.5
    )
    success_count = sum(decisions)
    print(f"初始金额:      ¥{initial_amount:,.2f}")
    print(f"持有年份:      {N}年")
    print(f"最终金额:      ¥{final_amount:,.2f}")
    print(f"决策序列:      {['✓' if d else '✗' for d in decisions]}")
    print(f"成功次数:      {success_count}/{N}")
    print(f"收益率:        {(final_amount - initial_amount) / initial_amount * 100:.2f}%")
    print()
    
    # ------ 模型2: 可能性空间 ------
    print("[模型2] 可能性空间分析 (1024种命运)")
    print("-" * 70)
    results = explore_possibility_space(initial_amount, success_multiplier, failure_multiplier, 1024)
    print(f"模拟次数:      {1024}")
    print(f"最小金额:      ¥{results['min_amount']:,.2f}")
    print(f"最大金额:      ¥{results['max_amount']:,.2f}")
    print(f"平均金额:      ¥{results['avg_amount']:,.2f}")
    print(f"中位数金额:    ¥{results['median_amount']:,.2f}")
    print(f"正收益命运:    {results['success_rate'] * 100:.2f}% ({int(results['success_rate'] * 1024)}/1024)")
    print(f"完美路径数:    {len(results['perfect_paths'])} (理论值: 1)")
    if results['perfect_paths']:
        print(f"  → 完美路径收益: ¥{results['perfect_paths'][0]:,.2f}")
    print()
    
    # ------ 模型3: 单一完美路径 ------
    print("[模型3] 单一完美路径计算")
    print("-" * 70)
    perfect_amount = calculate_perfect_path(initial_amount, success_multiplier)
    print(f"公式: {initial_amount} × ({success_multiplier}^{N})")
    print(f"完美路径最终金额: ¥{perfect_amount:,.2f}")
    print(f"理论收益率:      {(perfect_amount - initial_amount) / initial_amount * 100:.2f}%")
    print()
    
    # ------ 难度分析 ------
    print("[难度分析] 追求完美路径的成本")
    print("-" * 70)
    print(f"可能性空间大小:  2^{N} = {POSSIBILITY_SPACE}")
    print(f"完美路径概率:    1/{POSSIBILITY_SPACE} = {1/POSSIBILITY_SPACE * 100:.4f}%")
    print(f"失败路径数:      {POSSIBILITY_SPACE - 1} ({(1 - 1/POSSIBILITY_SPACE) * 100:.2f}%)")
    print()
    print("💡 解读:")
    print(f"  在{POSSIBILITY_SPACE}种投资命运中，只有1条完美路径。")
    print("  追求指数级回报的难度由此量化。")
    print("=" * 70)